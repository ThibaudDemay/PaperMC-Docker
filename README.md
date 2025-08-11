# PaperMC Docker

### TLDR;
- Base Image : [Amazon Corretto](https://hub.docker.com/_/amazoncorretto)
- Architecture : `amd64`, `arm64`
- Supported Tags : `latest`, `X.y`, `X.y.z`, `X.y.z-build`

## About

This project provides a set of Docker images for running a PaperMC Minecraft server.

The images are based on Amazon Corretto like the official [PaperMC docs](https://docs.papermc.io/misc/java-install) recommend and a specific version of the PaperMC server, which are downloaded from the official PaperMC build server.
Image are built using the `Dockerfile` in this repository and are pushed to Docker Hub under the `thibauddemay/papermc` namespace.

## Supported Tags

Each image is tagged with the version of the PaperMC server it contains and we also provide a group version using Major and Minor version `X.y` and `latest` tag that always points to the latest version.

| Tag      | Description                                  |
|----------|----------------------------------------------|
| `latest` | Latest version of PaperMC.                   |
| `X.y`    | Latest version of PaperMC in the X.y series. |
| `X.y.z`  | Specific version of PaperMC.                 |

## Usage

To help you get started creating a container from this image you can either use docker-compose or the docker cli.

The container expose the PaperMC server on port 25565.
You need to accept the EULA by setting the `EULA` environment variable to `true`.

We can customize the server configuration and access to server data by mounting a volume on `/app/data` and adding or modifying the server files.

### Docker Compose

```yaml
---
services:
  papermc-server:
    image: thibauddemay/papermc:latest
    restart: unless-stopped
    ports:
      - "25565:25565"
    environment:
      EULA: "true"
    volumes:
      - /path/to/papermc-data:/app/data
```

### Docker CLI

```bash
docker run -d \
  -name papermc-server \
  -p 25565:25565 \
  -e EULA="true" \ 
  -v /path/to/papermc-data:/app/data \
  --restart unless-stopped \
  thibauddemay/papermc:latest
```

## Options

| Environment Variable | Default       | Example       | Description                               |
|----------------------|---------------|---------------|-------------------------------------------|
| EULA                 | false         | true          | Set to true to accept the Minecraft EULA. |
| JAVA_ARGS            | -Xms4G -Xmx4G | -Xms2G -Xmx8G | Java arguments to pass to the server.     |