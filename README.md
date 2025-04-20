# Accreditation and Reporting System (API)

> ⚠️ **Note:** This repository has been archived and will no longer receive updates. For further information on the project's status and brand identity, please refer to the [organization's README](https://github.com/orgs/YCN-club).

The MIT-ARS, originally built for MIT Bengaluru, aims to reduce the manual work of information collection and handling that's required from institutions when applying for several nation-level accreditations.

This repository acts in conjunction with the [MIT-ARS Website](https://github.com/YCN-club/accreditation-website), and provides the API queries and responses required by the frontend to process and showcase data.

![Database Tables](/assets/db-tables.png)
*The database schema, which can also be found at [`/schema.sql`](/schema.sql).*

## Technologies Used

1. [Sanic](https://sanic.dev), a web framework for Python.
2. [Poetry](https://python-poetry.org/), for Python dependency management.
3. [PostgreSQL](https://www.postgresql.org), for data storage and organization.
4. [Docker](https://www.docker.com), for containerization and deployment.

## Product Demonstration

Details about the UI and demonstration can be found in the [frontend repository](https://github.com/YCN-club/accreditation-website).

## Development

Install the dependency manager.

```console
pip install poetry
```

Install the dependencies.

```console
poetry install
```

Configure the environment variables in `.env`.

```env
# Boolean to signal that the environment is Production (DEFAULTS TO FALSE)
IS_PROD=
# Name of Issues of JWT Token
HOST=DEMO
# Number of Trusted Proxies
PROXIES_COUNT=
# Postgres Server Host Address
DB_HOST=localhost
# Postgres Server Port
DB_PORT=5432
# Postgres Database Name
DB_NAME=ars
# Postgres Username
DB_USERNAME=root
# Postgres User Password
DB_PASSWORD=password
```

Generate an RSA key-pair.

```console
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

Run the development server using the following command.

```console
poetry run task server
```
