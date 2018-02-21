#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

#/ Usage: bash make_docs.sh
#/ Description: Recreates the documentation in docs/_build/html
#/ Options:
#/   --help: Display this help message
usage() { grep '^#/' "$0" | cut -c4- ; exit 0 ; }
expr "$*" : ".*--help" > /dev/null && usage

# Locate this script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cleanup() {
	if [ "$?" -ne 0 ]; then
		echo "Something went wrong."
	fi
}

if [[ "${BASH_SOURCE[0]}" = "$0" ]]; then
	cd ${SCRIPT_DIR}/../docs
	make html
	echo "Docs have been created in ${SCRIPT_DIR}/../docs/_build/html"
fi
