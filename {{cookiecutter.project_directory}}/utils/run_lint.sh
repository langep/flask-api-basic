#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

#/ Usage: bash run_lint.sh
#/ Description: Runs flake8 on {{cookiecutter.main_package_name}}
#/ Options:
#/   --help: Display this help message
#/ 	 --info: Displays used variables
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
	cd ${SCRIPT_DIR}/..
	export APP_CONFIG=${APP_CONFIG:-{{ cookiecutter.main_package_name }}.config.DevelopmentConfig}
	export FLASK_APP=${FLASK_APP:-${SCRIPT_DIR}/../autoapp.py}
	export FLASK_DEBUG=${FLASK_DEBUG:-1}

	if expr "$*" : ".*--help" > /dev/null; then
		echo -e "Using: "
		echo -e "\tAPP_CONFIG: "${APP_CONFIG}
		echo -e "\tFLASK_APP: "${FLASK_APP}
		echo -e "\tFLASK_DEBUG: "${FLASK_DEBUG}
	fi

	flask lint -f
fi
