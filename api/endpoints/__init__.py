from api.app import appserver

from .api.auth.callback import AuthCallback
from .api.auth.entra import AuthEntra
from .api.auth.login import AuthLogin
from .api.auth.sign_up import AuthSignUp
from .api.forms.root import FormsRoot

appserver.add_route(AuthEntra.as_view(), "/api/auth/entra")
appserver.add_route(AuthCallback.as_view(), "/api/auth/callback")
appserver.add_route(AuthLogin.as_view(), "/api/auth/login")
appserver.add_route(AuthSignUp.as_view(), "/api/auth/sign_up")
appserver.add_route(FormsRoot.as_view(), '/api/forms/<slug:str>')