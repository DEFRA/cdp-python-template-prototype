# cdp-python-template-prototype

Core Delivery Platform Python Backend Template.

This is work-in-progress. See [To Do List](./TODO.md)

- [cdp-python-template-prototype](#cdp-python-template-prototype)
  - [Requirements](#requirements)
    - [Docker](#docker)
    - [Python Dependencies](#python-dependencies)
  - [Local development](#local-development)
    - [Setup](#setup)
    - [Development](#development)
    - [Testing](#testing)
    - [Production](#production)
  - [API endpoints](#api-endpoints)
    - [Dependabot](#dependabot)
    - [SonarCloud](#sonarcloud)
  - [Licence](#licence)
    - [About the licence](#about-the-licence)

## Requirements

### Docker

This repository uses Docker throughout its lifecycle i.e. both for local development and the environments

This means that local installation of python and configuration of a python virtual environment is not required. Also environment variables are managed consistently throughout the lifecycle

See the `Dockerfile` and `compose.yml` for details

### Python Dependencies

This opinionated template uses the [`Fast API`](https://fastapi.tiangolo.com/) Python API framework.

This and all other python libraries must reside in `requirements.txt`

## Local development

Local development is done using Docker compose.  This template contains a local environment with:

- Localstack
- MongoDB
- This service

### Setup

Environment variables: `compose/aws.env``

Secrets: `compose/secrets.env`. You need to create this, as it's excluded from version control.

### Development

To run the application in `development` mode run:

```bash
docker compose watch
```

### Testing

To test the application run:

```bash
TBC
```

### Production

To mimic the application running in `production` mode locally run:

```bash
docker compose up --build -d
```

Stop the application with

```bash
docker compose down
```

## API endpoints

| Endpoint             | Description                    |
| :------------------- | :----------------------------- |
| `GET: /docs`         | Automatic API Swagger docs     |
| `GET: /`             | Simple example                 |

### Dependabot

We have added an example dependabot configuration file to the repository. You can enable it by renaming
the [.github/example.dependabot.yml](.github/example.dependabot.yml) to `.github/dependabot.yml`

### SonarCloud

Instructions for setting up SonarCloud can be found in [sonar-project.properties](./sonar-project.properties)

## Licence

THIS INFORMATION IS LICENSED UNDER THE CONDITIONS OF THE OPEN GOVERNMENT LICENCE found at:

<http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3>

The following attribution statement MUST be cited in your products and applications when using this information.

> Contains public sector information licensed under the Open Government license v3

### About the licence

The Open Government Licence (OGL) was developed by the Controller of Her Majesty's Stationery Office (HMSO) to enable
information providers in the public sector to license the use and re-use of their information under a common open
licence.

It is designed to encourage use and re-use of information freely and flexibly, with only a few conditions.
