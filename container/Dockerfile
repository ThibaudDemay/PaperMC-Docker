ARG JVM_VERSION=21-alpine

FROM amazoncorretto:${JVM_VERSION}

ARG PAPERMC_DOWNLOAD_URL

ENV JAVA_ARGS="-Xms4G -Xmx4G"

WORKDIR /app/data

COPY --chmod=0700 run.sh /app/run.sh

ADD $PAPERMC_DOWNLOAD_URL /app/paper.jar

EXPOSE 25565 25575

ENTRYPOINT ["/app/run.sh"]