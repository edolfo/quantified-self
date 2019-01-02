# Third party
import pymongo

# Internal lib
from lib.settings import Settings


class QuantSelfDB(object):
    def __init__(self, col_name):
        self.col_name = col_name
        return

    client = None

    @staticmethod
    def get_client():
        """
        Keep as a singleton to ensure a single connection pool
        """
        if QuantSelfDB.client is None:
            QuantSelfDB.client = pymongo.MongoClient(
                host=Settings.mongo_connection_string
            )
        return QuantSelfDB.client

    @property
    def database(self):
        client = QuantSelfDB.get_client()
        return client[Settings.db_name]

    @property
    def collection(self):
        return self.database[self.col_name]
