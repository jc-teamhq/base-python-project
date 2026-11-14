#!/usr/bin/env bash
# Test the template by generating projects from it:
#
#   1. every license choice renders and the project builds
#   2. no unrendered Jinja is left in a generated project
#   3. the default project passes its own full CI (scripts/ci.sh)
#
# The working tree is used as the template, uncommitted changes included.
# This is also the template repo's CI command.
set -euo pipefail

cd "$(dirname "$0")/.."
template="$PWD"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

generate() {  # generate <dest> [extra copier args...]
    local dest="$1"
    shift
    uv run --locked copier copy --quiet --defaults --vcs-ref HEAD \
        --data project_name=example-project \
        --data author_name="Template Test" \
        "$@" "$template" "$dest"
}

fail() {
    echo "FAIL: $*" >&2
    exit 1
}

echo "--- license choices"
# One per conditional LICENSE file (GPL-3.0-only shares the GPL branch).
for license in GPL-3.0-or-later MIT Apache-2.0 Proprietary; do
    dest="$work/license-$license"
    generate "$dest" --data license="$license"
    uv build --quiet --out-dir "$dest/dist" "$dest"
    if [[ "$license" == Proprietary ]]; then
        [[ ! -e "$dest/LICENSE" ]] || fail "$license: LICENSE should not exist"
        grep -q '"Private :: Do Not Upload"' "$dest/pyproject.toml" \
            || fail "$license: missing Private :: Do Not Upload classifier"
    else
        [[ -s "$dest/LICENSE" ]] || fail "$license: LICENSE missing or empty"
        grep -qx "license = \"$license\"" "$dest/pyproject.toml" \
            || fail "$license: license expression not set in pyproject.toml"
    fi
    echo "ok: $license"
done

echo "--- unrendered Jinja"
if grep -rnE '\{\{|\{%|%\}|\}\}' "$work/license-GPL-3.0-or-later" \
    --exclude-dir=dist --exclude-dir=.venv; then
    fail "unrendered Jinja (above)"
fi
echo "ok"

echo "--- full CI on the default project"
dest="$work/example-project"
generate "$dest"
cd "$dest"
git init --quiet
uv lock --quiet
git add --all  # pre-commit only checks files git knows about
scripts/ci.sh
