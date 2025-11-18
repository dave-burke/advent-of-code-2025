#!/bin/bash

set -e

DAY=${1}

if [[ -z "${DAY}" ]]; then
	echo "Usage: init-day.sh [day]"
	exit 1
fi

printf -v FILENAME "day%02d.py" $DAY

cp -v template.py "${FILENAME}"
chmod 755 "${FILENAME}"

