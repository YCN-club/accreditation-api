from api.app import appserver

from .api.auth.callback import AuthCallback
from .api.auth.entra import AuthEntra
from .api.auth.login import AuthLogin

appserver.add_route(AuthEntra.as_view(), "/api/auth/entra")
appserver.add_route(AuthCallback.as_view(), "/api/auth/callback")
appserver.add_route(AuthLogin.as_view(), "/api/auth/login")
