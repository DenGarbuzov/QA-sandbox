from func.base import *


@allure.title(Title.MAIN_ACTIVITY.value)
class TestEditProfile(AbstractTest):

    def set_up_class(self):
        self.go_to_edit_profile()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.MINER.value)
    def test_edit_profile_click_back_button(self):
        self.is_exist_by_element_id('')
        self.click_element_by_id('')
        allure.step('Проверка правильности перехода')
        self.is_exist_by_element_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="profile state",
                      attachment_type=AttachmentType.PNG)

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.MINER.value)
    def test_edit_profile_avatar_menu_close(self):
        self.open_avatar_in_edit_profile_options()
        if len(self.driver.find_elements_by_id('')) > 0:
            self.click_element_by_id('')
            self.wait_by_id('', 15)
            self.click_element_by_id('')
            self.wait_by_id('', 15)
        else:
            pass

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_edit_profile_name_edit(self):
        name_text = self.name_profile_block()
        old_name = self.get_text_by_obj(name_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="start name view",
                      attachment_type=AttachmentType.PNG)
        new_name = self.random_text(10)
        self.put_text_to_input_obj(new_name, name_text)
        self.click_done_options_done_button()
        assert self.get_text_by_id('') == new_name
        allure.attach(self.driver.get_screenshot_as_png(), name="edited name view",
                      attachment_type=AttachmentType.PNG)
        self.go_to_edit_profile()
        self.put_text_to_input_obj(old_name, name_text)
        self.click_done_options_done_button()
        allure.attach(self.driver.get_screenshot_as_png(), name="return start name",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id('') == old_name

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_edit_profile_login_edit(self):
        login_text = self.login_profile_block()
        old_name = self.get_text_by_obj(login_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="start login view",
                      attachment_type=AttachmentType.PNG)
        new_name = 'tessst'
        self.put_text_to_input_obj(new_name, login_text)
        self.click_done_options_done_button()
        assert self.get_text_by_id('') == new_name
        allure.attach(self.driver.get_screenshot_as_png(), name="edited login view",
                      attachment_type=AttachmentType.PNG)
        self.go_to_edit_profile()
        self.put_text_to_input_obj(old_name, login_text)
        self.click_done_options_done_button()
        allure.attach(self.driver.get_screenshot_as_png(), name="return login name",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id('') == old_name

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story(
        '')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_edit_profile_discription_random_text(self):
        about_profile_text = self.about_profile_block()
        old_name = self.get_text_by_obj(about_profile_text)
        allure.attach(self.driver.get_screenshot_as_png(), name="start about text",
                      attachment_type=AttachmentType.PNG)
        new_name = self.random_text(100)
        self.put_text_to_input_obj(new_name, about_profile_text)
        self.click_done_options_done_button()
        assert self.get_text_by_id('') == new_name
        allure.attach(self.driver.get_screenshot_as_png(), name="edited about text",
                      attachment_type=AttachmentType.PNG)
        self.go_to_edit_profile()
        self.put_text_to_input_obj(old_name, about_profile_text)
        self.click_done_options_done_button()
        allure.attach(self.driver.get_screenshot_as_png(), name="return start about text",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id('') == old_name

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.MINER.value)
    def test_edit_profile_discription_random_text_over_500(self):
        about_text_area = self.about_profile_block()
        input_text = self.random_text(700)
        self.put_text_no_clear_to_element_input(input_text, about_text_area)
        self.is_exist_by_element_id('')
        self.is_exist_by_element_id('')
        self.is_exist_by_element_id('')
        self.is_exist_by_element_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="error message",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('android:id/')
        assert about_text_area
