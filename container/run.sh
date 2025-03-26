#!/bin/bash

if [ -n "${EULA}" -a "${EULA}" = "true" ]; then
    echo "eula=true" > /app/eula.txt
fi

java -jar /app/paper.jar $@