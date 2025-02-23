from os import getenv

from dotenv import load_dotenv
from mayim.extension import SanicMayimExtension
from sanic.log import logger
from sanic_ext import Extend

from api.app import API, appserver
from api.mayim.auth_executor import AuthExecutor
from api.mayim.create_executor import CreateExecutor
from api.mayim.delete_executor import DeleteExecutor
from api.mayim.table_executor import TableExecutor
from api.mayim.user_executor import UserExecutor
from api.mayim.naac_executor import NAACExecutor
from api.mayim.nba_executor import NBAExecutor
from api.mayim.nirf_executor import NIRFExecutor

from . import endpoints  # noqa: F401

logger.debug("Loading ENV")
load_dotenv()

config = {}

# Read the public and private keys and add them to the config.
with open("public-key.pem") as public_key_file:
    config["PUB_KEY"] = public_key_file.read()

with open("private-key.pem") as private_key_file:
    config["PRIV_KEY"] = private_key_file.read()

# Try to get state from the ENV, defaults to being dev.
is_prod: str = config.get("IS_PROD", "false")

# Convert the string to a bool and update the config with the bool.
config.update({"IS_PROD": is_prod.lower() == "true"})

# Load default values for the database connection
config.update(
    {
        "DB_HOST": getenv("DB_HOST", "localhost"),
        "DB_PORT": int(getenv("DB_PORT", 5432)),
        "DB_USERNAME": getenv("DB_USERNAME", "root"),
        "DB_PASSWORD": getenv("DB_PASSWORD", "password"),
        "DB_NAME": getenv("DB_NAME", "helpdesk"),
        "HOST": getenv("HOST", "DEMO"),
    },
)

app: API = appserver
app.config.update(config)
app.config.PROXIES_COUNT = int(config.get("PROXIES_COUNT", 0))

Extend.register(
    SanicMayimExtension(
        executors=[
            AuthExecutor,
            UserExecutor,
            NAACExecutor,
            NBAExecutor,
            NIRFExecutor,
            CreateExecutor,
            TableExecutor,
            DeleteExecutor,
        ],
        dsn=f"postgres://{config['DB_USERNAME']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}",  # noqa: E501
    )
)


@app.listener("before_server_start")
async def setup_app(app: API):
    logger.info("Setup complete.")


if __name__ == "__main__":
    # Use a KWARGS dict to pass to app.run dynamically
    kwargs = {"access_log": True, "host": "0.0.0.0"}

    kwargs["debug"] = not app.config["IS_PROD"]
    kwargs["auto_reload"] = True
    # Run the API Server
    app.run(**kwargs)
