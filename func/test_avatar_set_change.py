from func.base import *


@allure.title(Title.MAIN_ACTIVITY.value)
class TestAvatarChange(AbstractTest):

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_set_avatar_library(self):
        allure.step('delete avatar if set')
        self.delete_avatar_if_set()
        allure.attach(self.driver.get_screenshot_as_png(), name="empty avatar",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('avatarImage', 15)
        self.click_element_by_id('')
        allure.step('')
        self.random_choice_crop_use_from_library()
        allure.attach(self.driver.get_screenshot_as_png(), name="avatar with photo",
                      attachment_type=AttachmentType.PNG)
        sleep(5)
        allure.step('assert set')
        self.click_element_by_id('')
        self.is_exist_by_element_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_set_avatar_camera(self):
        self.delete_avatar_if_set()
        allure.attach(self.driver.get_screenshot_as_png(), name="empty avatar",
                      attachment_type=AttachmentType.PNG)
        allure.step('')
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        allure.step('')
        self.take_camera_photo_crop()
        allure.attach(self.driver.get_screenshot_as_png(), name="avatar with photo",
                      attachment_type=AttachmentType.PNG)
        sleep(5)
        allure.step('')
        self.click_element_by_id('')
        self.is_exist_by_element_id('')
