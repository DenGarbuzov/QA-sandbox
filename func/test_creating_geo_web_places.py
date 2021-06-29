from func.base import *


@allure.title(Title.PLACE_ACTIVITY.value)
class TestCreatingPlaces(AbstractTest):

    def set_up_class(self):
        self.__go_to_create_web_geo_places()

    def __go_to_create_web_geo_places(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_geo_create_library_public(self):
        text = self.random_text(50)
        self.geo_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.random_choice_from_library()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="image set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_geo_create_library_drafts(self):
        text = self.random_text(50)
        self.geo_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.random_choice_from_library()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="image set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_geo_create_camera_public(self):
        text = self.random_text(50)
        self.geo_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.take_camera_photo_without_crop()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="image set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_geo_create_camera_drafts(self):
        text = self.random_text(50)
        self.geo_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.take_camera_photo_without_crop()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="image set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_web_create_camera_drafts(self):
        text = self.random_text(50)
        self.web_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.take_camera_photo_without_crop()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="image set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_web_create_camera_public(self):
        text = self.random_text(50)
        self.web_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.take_camera_photo_without_crop()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="image set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_web_create_library_drafts(self):
        text = self.random_text(50)
        self.web_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.random_choice_from_library()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="image set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_web_create_library_public(self):
        text = self.random_text(50)
        self.web_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.random_choice_from_library()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="image set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="confirm image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_web_create_screenshot_drafts(self):
        text = self.random_text(50)
        self.web_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.make_screenshot()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_web_create_screenshot_public(self):
        text = self.random_text(50)
        self.web_random_text_pre_config_without_photo(text)
        self.click_element_by_id('')
        self.make_screenshot()
        head_text = self.get_text_by_id('')
        self.category_random_chose_creating_place()
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot set",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.popup_close_if_exist()
        self.go_to_show_all_profile_places()
        new_one = self.choose_place_by_index_profile_all_places(0)
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot image",
                      attachment_type=AttachmentType.PNG)
        check_text = new_one.find_element_by_id('').text
        assert check_text == head_text
        self.delete_obj_longpress(new_one)
        try:
            self.click_element(new_one)
        except:
            EC.StaleElementReferenceException()