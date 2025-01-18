import jwt
from datetime import datetime, timedelta, timezone
from sanic import Sanic

from api.models.internal.jwt_data import JWT_Data
from api.models.internal.jwt_status import JWT_Status


class API(Sanic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def decode_jwt(self, jwt_token: str) -> JWT_Data:
        assert isinstance(jwt_token, str)
        data = JWT_Data(
            **jwt.decode(jwt_token, key=self.config["PUB_KEY"], algorithms="RS256")
        )
        return data

    def check_server_jwt(self, jwt_token: str) -> JWT_Status:
        if not jwt_token or jwt_token == "":
            return JWT_Status(authenticated=False, message="JWT Token not provided")
        try:
            jwt_data = self.decode_jwt(jwt_token)
        except jwt.exceptions.ImmatureSignatureError:
            # Raised when a tokens nbf claim represents a time in the future
            d = JWT_Status(
                authenticated=False, message="JWT Token not allowed to be used at time"
            )
        except jwt.exceptions.InvalidIssuedAtError:
            # Raised when a tokens iat claim is in the future
            d = JWT_Status(
                authenticated=False, message="JWT Token issued in the future"
            )
        except jwt.exceptions.ExpiredSignatureError:
            # Raised when a tokens exp claim indicates that it has expired
            d = JWT_Status(authenticated=False, message="JWT Token has expired")
        except jwt.exceptions.InvalidTokenError:
            # Generic invalid token
            d = JWT_Status(authenticated=False, message="JWT Token is invalid")
        else:
            # Valid Token
            d = JWT_Status(authenticated=True, JWT_Data=jwt_data)

        return d

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
