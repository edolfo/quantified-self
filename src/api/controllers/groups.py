# third-party libs
from flask import jsonify, request, make_response

# internal libs
from api import log
from lib.db.groups import Groups


def lst():
    grps = Groups().get_groups()
    return make_response(jsonify(grps), 200)
