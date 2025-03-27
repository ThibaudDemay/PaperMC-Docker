#!/usr/bin/env sh

if [ -n "${EULA}" -a "${EULA}" = "true" ]; then
    echo "eula=true" > /app/data/eula.txt
fi

java -jar $JAVA_ARGS /app/paper.jar -nogui $@