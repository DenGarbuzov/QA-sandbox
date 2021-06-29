from func.base import *


@allure.title(Title.PLACE_ACTIVITY.value)
class TestEditingPlaces(AbstractTest):

    def set_up_class(self):
        self.__go_to_create_web_geo_places()

    def __go_to_create_web_geo_places(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_geo_edit_public_library(self):
        text = self.random_text(50)
        self.geo_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.random_choice_from_library()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="create place info",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="save confirm",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.long_press_obj(new_one)
        self.click_element_by_id('')
        edit_text = self.random_text(40)
        self.place_content_edit(edit_text)
        self.category_random_chose_creating_place()
        self.edit_content_photo_place()
        self.random_choice_from_library()
        self.assert_adding_photo_in_all_photo_place_view()
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm adding content",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm new info",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        edited_place = self.choose_place_by_index_profile_all_places(0)
        assert edit_text == edited_place.find_element_by_id('').text
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm editing",
                      attachment_type=AttachmentType.PNG)
        self.delete_obj_longpress(edited_place)
        sleep(2)
        try:
            self.click_element(edited_place)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_geo_edit_public_photo(self):
        text = self.random_text(50)
        self.geo_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.random_choice_from_library()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="create place info",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="save confirm",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.long_press_obj(new_one)
        self.click_element_by_id('')
        edit_text = self.random_text(40)
        self.place_content_edit(edit_text)
        self.category_random_chose_creating_place()
        self.edit_content_photo_place()
        self.take_camera_photo_without_crop()
        self.assert_adding_photo_in_all_photo_place_view()
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm adding content",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm new info",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        edited_place = self.choose_place_by_index_profile_all_places(0)
        assert edit_text == edited_place.find_element_by_id('').text
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm editing",
                      attachment_type=AttachmentType.PNG)
        self.delete_obj_longpress(edited_place)
        sleep(2)
        try:
            self.click_element(edited_place)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_web_edit_screenshot_public(self):
        text = self.random_text(50)
        self.web_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.make_screenshot()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="create place info",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="save confirm",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.long_press_obj(new_one)
        self.click_element_by_id('')
        edit_text = self.random_text(40)
        self.place_content_edit(edit_text)
        self.category_random_chose_creating_place()
        self.edit_content_photo_place()
        self.make_screenshot()
        self.assert_adding_photo_in_all_photo_place_view()
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm adding content",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm new info",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        edited_place = self.choose_place_by_index_profile_all_places(0)
        assert edit_text == edited_place.find_element_by_id('').text
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm editing",
                      attachment_type=AttachmentType.PNG)
        self.delete_obj_longpress(edited_place)
        sleep(2)
        try:
            self.click_element(edited_place)
        except:
            EC.StaleElementReferenceException()
