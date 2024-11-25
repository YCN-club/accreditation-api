import aiohttp
import json
import jwt
from datetime import datetime, timedelta, timezone
from sanic import Sanic
from sanic.log import logger


class API(Sanic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx.entra_public_keys = dict()

    def get_entra_jwt_keys(self) -> dict:
        return self.ctx.entra_public_keys

    async def load_entra_jwks(self):
        # Fetch OpenID Configuration of Entra
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://login.microsoftonline.com/common/.well-known/openid-configuration"
            ) as resp:
                config = await resp.json()
                jwks_uri = config["jwks_uri"]

        logger.info(
            "Fetching JSON Web Key Set (JWKS) from the OpenID Configuration of Entra"
        )

        # Fetch the JSON Web Key Set (JWKS) from the OpenID Configuration of Entra
        async with aiohttp.ClientSession() as session:
            async with session.get(jwks_uri) as resp:
                jwks = await resp.json()

        logger.info("Saving public keys from the JWKS")

        # Create a dictionary of public keys from the JWKS
        public_keys = {}
        for jwk in jwks["keys"]:
            kid = jwk["kid"]
            public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
        self.ctx.entra_public_keys = public_keys

    async def generate_jwt(
        self,
        data: dict,
        validity: int,
    ) -> str:
        """Generates JWT with given data"""
        now = datetime.now(timezone.utc)
        expire = now + timedelta(minutes=validity)
        iss = f"ARS_API_{self.config['HOST']}"
        data.update({"exp": expire, "iat": now, "nbf": now, "iss": iss})
        return jwt.encode(data, self.config["PRIV_KEY"], algorithm="RS256")


appserver = API("API")
