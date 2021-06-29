from func.base import *


@allure.title(Title.MAIN_ACTIVITY.value)
class TestPublishUnpublishPlace(AbstractTest):

    def set_up_class(self):
        self.__go_to_create_web_geo_places()

    def __go_to_create_web_geo_places(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_publish_created_place(self):
        text = self.random_text(15)
        self.geo_random_text_pre_config_without_photo(text)
        head_text = self.get_text_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="created place",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        allure.attach(self.driver.get_screenshot_as_png(), name="drafts confirm save",
                      attachment_type=AttachmentType.PNG)
        new_one = self.choose_place_by_index_profile_all_places(0)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text

        ''' переделать тесты подобрать id без нижних пробелов'''

        self.long_press_options_publish_click(new_one)

        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm publish",
                      attachment_type=AttachmentType.PNG)
        published_place = self.choose_place_by_index_profile_all_places(0)
        confirm_place = published_place.find_element_by_id('').text
        assert confirm_place == check_text
        self.delete_obj_longpress(published_place)
        sleep(2)
        try:
            self.click_element(published_place)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_unpublish_created_place(self):
        text = self.random_text(15)
        self.geo_random_text_pre_config_without_photo(text)
        head_text = self.get_text_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="created place",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text

        ''' переделать тесты подобрать id без нижних пробелов'''
        self.long_press_options_unpublish_click(new_one)

        self.click_element_by_id('')
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm unpublish",
                      attachment_type=AttachmentType.PNG)
        unpublished_place = self.choose_place_by_index_profile_all_places(0)
        confirm_place = unpublished_place.find_element_by_id('').text
        assert confirm_place == check_text
        self.delete_obj_longpress(unpublished_place)
        sleep(2)
        try:
            self.click_element(unpublished_place)
        except:
            EC.StaleElementReferenceException()

