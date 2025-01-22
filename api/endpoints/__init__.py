from api.app import appserver

from .api.auth.login import AuthLogin
from .api.auth.register import AuthRegister
from .api.forms.root import FormsRoot

appserver.add_route(AuthLogin.as_view(), "/api/auth/login")
appserver.add_route(AuthRegister.as_view(), "/api/auth/register")
appserver.add_route(FormsRoot.as_view(), "/api/forms/<slug:strorempty>")
