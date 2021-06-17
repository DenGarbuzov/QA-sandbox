class Capabilities:
    _capabilities = {
        'platformName': 'Android',
        # in seconds
        'deviceReadyTimeout': 20,
        # in seconds
        'androidDeviceReadyTimeout': 20,
        # in milliseconds
        'appWaitDuration': 30000,
        # in seconds
        'autoGrantPermissions': 'true',
        # to avoid permission issues
        'disableWindowAnimation': 'true',
        # to speed up tests
        'gpsEnabled': 'true'
        # to use emulation device location
    }

    @staticmethod
    def builder():
        return Capabilities()

    def build(self):
        return self._capabilities

    def set_start_activity(self, package: str, activity: str):
        self._capabilities['appPackage'] = package
        self._capabilities['appActivity'] = activity
        return self

    def set_api_version(self, version: int):
        self._capabilities['platformVersion'] = str(version)
        return self

    def set_android_version(self, version: str):
        self._capabilities['version'] = version
        return self

    def set_id(self, device_id: int):
        self._capabilities['udid'] = str(device_id)
        return self

    def set_path_to_apk(self, path: str):
        self._capabilities['app'] = path
        return self

    def set_device_name(self, device_name: str):
        self._capabilities['deviceName'] = device_name
        return self

    def set_adb_port(self, port: int):
        self._capabilities['adbPort'] = str(port)
        return self

    def set_remote_adb_host(self, remote_host: str):
        self._capabilities['remoteAdbHost'] = remote_host
        return self

    def set_device_ready_timeout(self, ready_timeout: int):
        """
        :param ready_timeout:  in seconds
        """
        self._capabilities['deviceReadyTimeout'] = str(ready_timeout)
        return self

    def set_no_reset(self, is_no_reset: bool):
        self._capabilities['noReset'] = str(is_no_reset)
        return self

    def set_full_reset(self, is_full_reset: bool):
        self._capabilities['fullReset'] = str(is_full_reset)
        return self

    def set_locale(self, locale: str):
        self._capabilities['locale'] = locale
        return self

    def set_language(self, language: str):
        self._capabilities['language'] = language
        return self
