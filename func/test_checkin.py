from func.base import *


@allure.title(Title.MAIN_ACTIVITY.value)
class TestCheckin(AbstractTest):

    def set_up_class(self):
        self.__go_to_create_web_geo_places()

    def __go_to_create_web_geo_places(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story(' ')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_checkin_geo(self):
        text = self.random_text(10)
        self.geo_random_text_pre_config_without_photo(text)
        head_text = self.get_text_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="geo name",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm name",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        new_one.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.wait_by_id('',15)
        self.click_element_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="checkin",
                      attachment_type=AttachmentType.PNG)
        checkin = self.driver.find_elements_by_id('')[0]
        assert text in self.get_text_by_obj(checkin)
        self.driver.swipe(start_x=1302, start_y=464, end_x=167, end_y=478)
        if len(self.driver.find_elements_by_id('')) > 0:
            assert text not in self.get_text_by_id('')[0]
        else:
            self.click_element_by_id('')
            self.not_exist_by_id('')
            self.not_exist_by_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_checkin_web(self):
        text = self.random_text(10)
        self.web_random_text_pre_config_without_photo(text)
        head_text = self.get_text_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="web name",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm name",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        new_one.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="checkin",
                      attachment_type=AttachmentType.PNG)
        checkin = self.driver.find_elements_by_id('')[0]
        assert text in self.get_text_by_obj(checkin)
        self.driver.swipe(start_x=1302, start_y=464, end_x=167 , end_y=478)
        if len(self.driver.find_elements_by_id('')) > 0:
            assert text not in self.get_text_by_id('')[0]
        else:
            self.click_element_by_id('')
            self.not_exist_by_id('')
            self.not_exist_by_id('')
