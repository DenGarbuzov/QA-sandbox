from func.base import *


@allure.title(Title.MAIN_ACTIVITY.value)
class TestSubscriptions(AbstractTest):

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_subscribe(self):
        search_data = self.random_profile()
        self.click_element_by_id('')
        self.wait_by_id('',15)
        allure.attach(self.driver.get_screenshot_as_png(), name="subscribers count",
                      attachment_type=AttachmentType.PNG)
        if len(self.driver.find_elements_by_xpath("//*[@text='" + search_data + "']")) > 0:

            profile = self.driver.find_element_by_xpath("//*[@text='" + search_data + "']")
            assert profile
            image = profile.parent.find_element_by_id('')
            image.click()
            self.click_element_by_id('')
            sleep(1)
            self.click_element_by_id('')
            sleep(2)
            self.click_element_by_id('')
            sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name="unsubscribed successful",
                          attachment_type=AttachmentType.PNG)
            assert len(self.driver.find_elements_by_xpath("//*[@text='" + search_data + "']")) <= 0

        else:
            self.click_element_by_id('')
            self.go_to_global_search()
            search_data = self.random_profile()
            self.put_text_to_input(search_data, '')
            allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
            self.wait_by_id('', 15)
            common_output_block = self.driver.find_element_by_id('')
            first_search_output_block = \
            common_output_block.find_elements_by_class_name('android.widget.FrameLayout')[0]
            first_search_output_block.click()
            self.wait_by_id('', 15)
            allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
            assert self.get_text_by_id('') == search_data
            self.click_element_by_id('')
            sleep(1)
            self.click_element_by_id('')
            sleep(2)
            self.click_element_by_id('')
            sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name="subscribed successful",
                          attachment_type=AttachmentType.PNG)
            assert len(self.driver.find_elements_by_xpath("//*[@text='" + search_data + "']")) > 0

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_unsubscribe(self):
        search_data = self.random_profile()
        self.click_element_by_id('')
        self.wait_by_id('',15)
        allure.attach(self.driver.get_screenshot_as_png(), name="subscribers count",
                      attachment_type=AttachmentType.PNG)
        if len(self.driver.find_elements_by_xpath("//*[@text='" + search_data + "']")) > 0:
            profile = self.driver.find_element_by_xpath("//*[@text='" + search_data + "']")
            assert profile
            image = profile.parent.find_element_by_id('')
            image.click()
            self.click_element_by_id('')
            sleep(1)
            self.click_element_by_id('')
            sleep(2)
            self.click_element_by_id('')
            sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name="unsubscribed successful",
                          attachment_type=AttachmentType.PNG)
            assert len(self.driver.find_elements_by_xpath("//*[@text='" + search_data + "']")) <= 0

        else:
            self.click_element_by_id('')
            self.go_to_global_search()
            search_data = self.random_profile()
            self.put_text_to_input(search_data, '')
            allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
            self.wait_by_id('', 15)
            common_output_block = self.driver.find_element_by_id('')
            first_search_output_block = \
            common_output_block.find_elements_by_class_name('')[0]
            first_search_output_block.click()
            self.wait_by_id('', 15)
            allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
            assert self.get_text_by_id('') == search_data
            self.click_element_by_id('')
            sleep(1)
            self.click_element_by_id('')
            sleep(2)
            self.click_element_by_id('')
            sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name="subscribed successful",
                          attachment_type=AttachmentType.PNG)
            assert len(self.driver.find_elements_by_xpath("//*[@text='" + search_data + "']")) > 0