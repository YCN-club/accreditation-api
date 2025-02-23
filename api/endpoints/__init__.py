from api.app import appserver

from .api.auth.login import AuthLogin
from .api.auth.register import AuthRegister
from .api.forms.root import FormsRoot
from .api.fetch.tables import TablesRoot
from .api.fetch.naac import NAACFetch
from .api.fetch.nba import NBAFetch
from .api.fetch.nirf import NIRFFetch
from .api.summary import SummaryRoot


appserver.add_route(AuthLogin.as_view(), "/api/auth/login")
appserver.add_route(AuthRegister.as_view(), "/api/auth/register")
appserver.add_route(FormsRoot.as_view(), "/api/forms/<slug:strorempty>")
appserver.add_route(TablesRoot.as_view(), "/api/tables/<slug:strorempty>")
appserver.add_route(NAACFetch.as_view(), "/api/fetch/naac/<slug:strorempty>")
appserver.add_route(NBAFetch.as_view(), "/api/fetch/nba/<slug:strorempty>")
appserver.add_route(NIRFFetch.as_view(), "/api/fetch/nirf/<slug:strorempty>")
appserver.add_route(SummaryRoot.as_view(), "/api/summary")
