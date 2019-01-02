import os
import logging
import sys
sys.path.append(os.path.abspath('../lib'))

FORMAT = '{levelname:8} {asctime:25} {pathname:30.29}{lineno} {message}'
logging.basicConfig(level=logging.INFO, format=FORMAT, style='{')

log = logging.getLogger()
