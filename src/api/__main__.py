# stdlib
import io
import os
import yaml

# third-party lib
import connexion
from flask import current_app

# internal lib
from api import log

options = {"swagger_ui": True}
app = connexion.FlaskApp(__name__, options=options)
BASE_SCHEMA = 'base.yml'


def load_schemas():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    schema_files = os.listdir(os.path.join(dir_path, 'schemas'))

    with io.open(os.path.join(dir_path, 'schemas', BASE_SCHEMA), 'r') as base_api:
        api = yaml.load(base_api)

    for file in schema_files:
        if file == BASE_SCHEMA:
            continue

        with io.open(os.path.join(dir_path, 'schemas', file), 'r') as extension_file:
            api_ext = yaml.load(extension_file)

        if 'definitions' in api_ext:
            api['definitions'] = {**api['definitions'], **api_ext['definitions']}
        if 'paths' in api_ext:
            api['paths'] = {**api['paths'], **api_ext['paths']}
    try:
        outfile = 'generated.api.yml'
        with io.open(os.path.join(dir_path, outfile), 'w') as generated_api_file:
            yaml.dump(api, generated_api_file)
            return outfile
    except Exception as e:
        current_app.schema_info['status'] = 'error'
        current_app.schema_info['message'] = str(e)
        return False


if __name__ == '__main__':
    log.info('Starting server')
    api_file = load_schemas()
    if api_file:
        app.add_api(api_file)
    else:
        log.error('Error in initializing swagger specification')

    host = '0.0.0.0'
    port = 6001
    app.run(host=host, port=port)
    log.info(f'API server running on {host}:{port}')
