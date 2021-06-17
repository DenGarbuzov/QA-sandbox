import os

import pytest
from appium import webdriver

from adb_utils import android_api_by_device_id
from capabilities import Capabilities
from read_json_utils import read_config_file, SERVICE_DIR_PATH, prepare_device, read_json_value, RESOURCE_DIR_PATH


@pytest.fixture(scope='session')
def fix_login(fix_config):
    return read_json_value(fix_config, 'login')


@pytest.fixture(scope='session')
def fix_password(fix_config):
    return read_json_value(fix_config, 'password')


@pytest.fixture(scope='session')
def fix_service_folder_path():
    if not os.path.exists(SERVICE_DIR_PATH):
        os.makedirs(SERVICE_DIR_PATH)
    return SERVICE_DIR_PATH


@pytest.fixture(scope='session')
def fix_config():
    return read_config_file()


@pytest.fixture(scope='session')
def fix_apk_path(fix_config):
    for root, dirs, files in os.walk(RESOURCE_DIR_PATH):
        for file in files:
            if file.endswith(".apk"):
                return os.path.join(root, file)
    raise ValueError('Apk file not found!')


@pytest.fixture(scope='session')
def fix_package_name(fix_config):
    return read_json_value(fix_config, 'package_name')


@pytest.fixture(scope='session')
def fix_start_activity(fix_config):
    return read_json_value(fix_config, 'start_activity')


@pytest.fixture(scope='session')
def fix_is_delete_app(fix_config):
    return read_json_value(fix_config, 'is_delete_app')


def shutdown(device_driver: webdriver ) -> None:
    device_driver.quit()


def prepare_driver(version_or_id, selenoid_hub, package_name, apk_path, is_delete_app, start_activity):
        api_version = android_api_by_device_id(version_or_id)

        prepare_device(version_or_id, package_name, is_delete_app, apk_path)

        capabilities = Capabilities.builder() \
            .set_id(version_or_id) \
            .set_api_version(api_version) \
            .set_path_to_apk(apk_path) \
            .set_start_activity(package_name, start_activity) \
            .build()
        device_driver: webdriver = webdriver.Remote(selenoid_hub, capabilities)
        return device_driver


@pytest.yield_fixture(autouse=True)
def driver(request, fix_selenoid_hub, fix_package_name, fix_apk_path,
           fix_is_delete_app, fix_version_or_id, fix_start_activity):
    device_driver = prepare_driver(version_or_id=fix_version_or_id,
                                   selenoid_hub=fix_selenoid_hub, package_name=fix_package_name,
                                   apk_path=fix_apk_path, is_delete_app=fix_is_delete_app,
                                   start_activity=fix_start_activity)
    request.cls.driver = device_driver
