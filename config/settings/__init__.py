import os

PRODUCTION_SERVER_ROLE = "production"

if os.getenv("SERVER_ROLE", "") == PRODUCTION_SERVER_ROLE:
    from .prod import *
else:
    from .dev import *
