from datetime import datetime


class JWT_Data:
    def __init__(
        self, name, email, roles, exp, iat, nbf, iss, uuid: str = None
    ) -> None:
        # Make sure none of the values are None
        if None in (name, email, roles, exp, iat, nbf, iss):
            raise ValueError("All values must be provided")
        # If role is "signup" then UUID is not needed
        if uuid is None and "signup" not in roles:
            raise ValueError("UUID is required for all roles except 'signup'")
        self.name = name
        self.email = email
        self.uuid = uuid
        self.roles = roles
        self.exp = datetime.fromtimestamp(exp)
        self.iat = datetime.fromtimestamp(iat)
        self.nbf = datetime.fromtimestamp(nbf)
        self.iss = iss

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "roles": self.roles,
        }
