import enum
import uuid
from abc import abstractmethod
from enum import Enum
import random
from time import sleep

import pytest
import string

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('driver')
class AbstractTest(object):
    driver: webdriver = None

    def click_element(self, element) -> bool:
        self.wait_element(element, 30)
        button = self.driver.find_element(element)
        if button and button.is_enabled():
            button.click()
            return True
        return False