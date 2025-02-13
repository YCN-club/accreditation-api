from api.app import appserver

from .api.auth.callback import AuthCallback
from .api.auth.entra import AuthEntra
from .api.auth.login import AuthLogin
from .api.auth.sign_up import AuthSignUp
from .api.forms.root import FormsRoot
from .api.fetch.naac import NAACFetch
from .api.fetch.nba import NBAFetch
from .api.fetch.nirf import NIRFFetch


appserver.add_route(AuthEntra.as_view(), "/api/auth/entra")
appserver.add_route(AuthCallback.as_view(), "/api/auth/callback")
appserver.add_route(AuthLogin.as_view(), "/api/auth/login")
appserver.add_route(AuthSignUp.as_view(), "/api/auth/sign_up")
appserver.add_route(FormsRoot.as_view(), "/api/forms/<slug:strorempty>")
appserver.add_route(NAACFetch.as_view(), "/api/fetch/naac/<slug:strorempty>")
appserver.add_route(NBAFetch.as_view(), "/api/fetch/nba/<slug:strorempty>")
appserver.add_route(NIRFFetch.as_view(), "/api/fetch/nirf/<slug:strorempty>")
