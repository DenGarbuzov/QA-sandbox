from func.base import *


@allure.title(Title.MAIN_ACTIVITY.value)
class TestNavigation(AbstractTest):

    def set_up_class(self):
        self.go_to_global_search()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_google_maps(self):
        search_data = 'The_place_to_find'
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
        sleep(2)
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        sleep(1)
        all_buttons = self.driver.find_elements_by_id('')
        google_maps = all_buttons[0]
        google_maps.click()
        allure.attach(self.driver.get_screenshot_as_png(), name="result",
                      attachment_type=AttachmentType.PNG)
        self.is_exist_by_element_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_yandex_maps(self):
        search_data = 'The_place_to_find'
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('', 15)
        sleep(2)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
            common_output_block.find_elements_by_class_name('android.widget.FrameLayout')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        sleep(1)
        all_buttons = self.driver.find_elements_by_id('')
        yandex_maps = all_buttons[1]
        yandex_maps.click()
        allure.attach(self.driver.get_screenshot_as_png(), name="result",
                      attachment_type=AttachmentType.PNG)
        assert '' in self.driver.find_element_by_id('').text

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_yandex_navigator(self):
        search_data = 'The_place_to_find'
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('', 15)
        sleep(2)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
            common_output_block.find_elements_by_class_name('')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        sleep(1)
        all_buttons = self.driver.find_elements_by_id('')
        yandex_navigator = all_buttons[2]
        yandex_navigator.click()
        allure.attach(self.driver.get_screenshot_as_png(), name="result",
                      attachment_type=AttachmentType.PNG)
        assert '' in self.driver.find_element_by_id('').text