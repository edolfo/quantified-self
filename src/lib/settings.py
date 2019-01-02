import os
import yaml


class Settings(object):
    config = yaml.load(open(os.environ.get('CONFIG_PATH'), 'r'))

    mongo_connection_string = config['mongo']['connection_string']
    db_name = config['mongo']['db_name']
