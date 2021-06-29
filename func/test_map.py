from func.base import *


@allure.title(Title.MAP_ACTIVITY.value)
class TestMapActivity(AbstractTest):

    @allure.feature(Feature.CHECK_EXIST_ELEMENT.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_open_mw(self):
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.is_exist_by_element_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)

    @allure.feature(Feature.CLICK_ELEMENT.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_open_profile_map(self):
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.is_exist_by_element_id('viewMap')
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_open_someones_map(self):
        self.go_to_global_search()
        search_data = ''
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
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.is_exist_by_element_id('')
