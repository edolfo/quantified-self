# Internal lib
from lib.db.base import QuantSelfDB


class Groups(QuantSelfDB):
    def __init__(self):
        super().__init__('groups')

    def get_groups(self):
        col = self.collection
        results = list(col.find())
        for r in results:
            r['id'] = str(r['_id'])
            del r['_id']
        return results
