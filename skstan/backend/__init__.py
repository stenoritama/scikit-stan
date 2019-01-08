import json
import os

TMP_DIR = '/tmp'

SKSTAN_HOME_ENV_VAR = 'SKSTAN_HOME'
SKSTAN_DIR = '.skstan'
SKSTAN_JSON = 'skstan.json'

DEFAULT_BACKGROUND = 'stan'


def has_write_permission(dir_name):
    return os.access(dir_name, os.W_OK)


def extract_skstan_config(skstan_dir):
    config_file_path = os.path.join(skstan_dir, SKSTAN_JSON)
    if os.path.exists(config_file_path):
        with open(config_file_path) as f:
            return json.load(f)


# if SKSTAN_HOME environment variable exists, use its value as skstan dir.
if SKSTAN_HOME_ENV_VAR in os.environ:
    _skstan_dir = os.environ.get(SKSTAN_HOME_ENV_VAR)
else:
    _base_dir = os.path.expanduser('~')
    if has_write_permission(_base_dir):
        _skstan_dir = os.path.join(_base_dir, SKSTAN_DIR)
    else:
        _skstan_dir = TMP_DIR

try:
    _config_json = extract_skstan_config(_skstan_dir)
    _CURRENT_BACKEND = _config_json['backend']
except KeyError:
    _CURRENT_BACKEND = DEFAULT_BACKGROUND
