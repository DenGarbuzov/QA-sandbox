import json
import os
import pathlib
from pathlib import Path
from pytest_utils import fail
from install_config import is_exist_app, uninstall_apk, install_apk


PROJECT_ROOT_PATH = pathlib.Path(__file__).parent.parent.absolute()
SERVICE_DIR_PATH = os.path.join(PROJECT_ROOT_PATH, 'tmp')
RESOURCE_DIR_PATH = os.path.join(PROJECT_ROOT_PATH, 'apk')


def read_config_file():
    local_file_config = Path(os.path.join(PROJECT_ROOT_PATH, 'config_local.json'))
    if local_file_config.exists():
        file_config = local_file_config
    else:
        file_config = Path(os.path.join(PROJECT_ROOT_PATH, 'config.json'))
    if file_config.is_file() is False:
        fail('Конфигурационный файл не найден!')
    with open(file_config) as config_file:
        data = json.load(config_file)
    return data


def read_json_value(config: json, name: str):
    if config[name] is None:
        raise Exception('The json "{}" does not contain key "{config["{}"]}"'.format(json, name))
    return config[name]


def prepare_device(device_id, package_name, is_delete_app, path_to_apk):
    if is_delete_app and is_exist_app(device_id, package_name):
        if not uninstall_apk(device_id, package_name):
            fail('Не удалось удалить приложение!')

    if not is_exist_app(device_id, package_name):
        if not install_apk(device_id, path_to_apk):
            fail('Не удалось установить приложение!')

