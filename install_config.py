from adb_utils import available_devices, android_api_by_device_id, install_apk, uninstall_apk, is_exist_app


def test_android_api_by_device_id() -> None:
    devices = available_devices()
    assert len(devices) > 0

    version = android_api_by_device_id(devices[0])
    assert version > 0


def test_install_apk(fix_apk_path) -> None:
    devices = available_devices()
    assert len(devices) > 0

    is_install = install_apk(devices[0], fix_apk_path)
    assert is_install


def test_is_exist_app(fix_package_name, fix_apk_path) -> None:
    devices = available_devices()
    assert len(devices) > 0

    assert install_apk(devices[0], fix_apk_path)
    assert is_exist_app(devices[0], fix_package_name)


def test_uninstall_apk(fix_package_name) -> None:
    devices = available_devices()
    assert len(devices) > 0

    is_uninstall = uninstall_apk(devices[0], fix_package_name)
    assert is_uninstall


def test_available_devices(fix_apk_path) -> None:
    devices = available_devices()
    assert len(devices) > 0
