import os

SUCCESS_MESSAGE = 'Success'


def available_devices() -> list:
    try:
        raw_devices = os.popen('adb devices').read().split('\n', 1)[1].split('device')
        return list(filter(lambda x: x != '', list(map(lambda x: x.strip(), raw_devices))))
    except Exception as ex:
        print(ex)
        return list()


def uninstall_apk(device_id: str, package_name: str) -> bool:
    is_install = False
    try:
        is_install = SUCCESS_MESSAGE in os.popen('adb -s {} uninstall {}'.format(device_id, package_name)).read()
    finally:
        return is_install


def install_apk(device_id: str, path_to_apk: str) -> bool:
    is_install = False
    try:
        is_install = SUCCESS_MESSAGE in os.popen(f"adb -s '{device_id}' install -t '{path_to_apk}'").read()
    finally:
        return is_install


def is_exist_app(device_id: str, package_name: str) -> bool:
    is_exist = False
    try:
        is_exist = package_name == os.popen('adb -s {} shell pm list packages com.planet.'
                                            .format(device_id, package_name)) \
            .read() \
            .replace('package:', '') \
            .replace('\n', '') \
            .strip()
    finally:
        return is_exist


def android_api_by_device_id(device_id: str) -> int:
    try:
        version = os.popen('adb -s {} shell getprop ro.build.version.release'.format(device_id)).read().strip()
        if version.isnumeric():
            return int(version)
        else:
            raise Exception('Android API version is not number!')
    except Exception as ex:
        print(ex)
        return -1
