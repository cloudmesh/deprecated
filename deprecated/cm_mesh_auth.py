from cloudmesh.cm_mongo import cm_MongoBase
from cloudmesh.config.cm_config import cm_config_server, get_mongo_db
from cloudmesh.util.logger import LOGGER
import pprint


# ----------------------------------------------------------------------
# SETTING UP A LOGGER
# ----------------------------------------------------------------------

log = LOGGER(__file__)

class cm_userauth(cm_MongoBase):

    def __init__(self):
        self.cm_type = "userauth"
        # self.db_userauth = get_mongo_db(self.cm_type)
        self.connect()
        self.db_userauth = self.db_mongo


