from func.base import *


@allure.title(Title.BACKGROUND.value)
class TestBackground(AbstractTest):

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_background_set_library(self):
        self.delete_background_if_set()
        self.background_set()
        self.random_choice_crop_use_from_library()
        allure.attach(self.driver.get_screenshot_as_png(), name="background set",
                      attachment_type=AttachmentType.PNG)
        sleep(2)
        self.not_exist_by_id('')

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_background_set_photo(self):
        self.delete_background_if_set()
        self.background_set()
        self.take_camera_photo_crop()
        allure.attach(self.driver.get_screenshot_as_png(), name="background set",
                      attachment_type=AttachmentType.PNG)
        sleep(2)
        self.not_exist_by_id('')
