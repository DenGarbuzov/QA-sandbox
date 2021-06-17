from methods import *
import pytest



@pytest.mark.usefixtures('driver')
def test_click_element(self):
    a = self.driver.find_element_by_id('')
    a.click()

