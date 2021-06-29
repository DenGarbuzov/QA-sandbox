from func.base import *

@allure.title(Title.PLACE_ACTIVITY.value)
class TestPlacesDescription(AbstractTest):

    def set_up_class(self):
        self.__go_to_create_web_geo_places()

    def __go_to_create_web_geo_places(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_geo_place_description(self):
        text = self.random_text(50)
        self.geo_random_text_pre_config_without_photo(text)
        # head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="create place info",
                      attachment_type=AttachmentType.PNG)
        description_text = self.get_text_by_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="save confirm",
                      attachment_type=AttachmentType.PNG)
        new_one.click()
        self.wait_by_id('',15)
        self.scroll_down_to_id('')
        check_description = self.get_text_by_id('')
        assert description_text == check_description
        self.click_element_by_id('')
        edited_place = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm editing",
                      attachment_type=AttachmentType.PNG)
        self.delete_obj_longpress(edited_place)
        sleep(2)
        try:
            self.click_element(edited_place)
        except:
            EC.StaleElementReferenceException()