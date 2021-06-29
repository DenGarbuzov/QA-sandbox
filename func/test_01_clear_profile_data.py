from func.base import *


@allure.title(Title.MAIN_ACTIVITY.value)
class TestWipeData(AbstractTest):

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_wipe_draft_places(self):
        self.go_to_drafts_from_profile()
        sleep(2)
        self.swipe_up()
        sleep(2)
        if len(self.driver.find_elements_by_id()) > 0:
            self.go_to_drafts_all_places()
            allure.attach(self.driver.get_screenshot_as_png(), name="initial amount",
                      attachment_type=AttachmentType.PNG)
            self.delete_all_places()
            allure.attach(self.driver.get_screenshot_as_png(), name="wipe result",
                      attachment_type=AttachmentType.PNG)
        else:
            pass


    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_wipe_draft_collections(self):
        self.go_to_drafts_from_profile()
        sleep(2)
        if len(self.driver.find_elements_by_id()) > 0:
            self.go_to_all_collections_in_drafts()
            allure.attach(self.driver.get_screenshot_as_png(), name="initial amount",
                      attachment_type=AttachmentType.PNG)
            self.delete_all_collections()
            allure.attach(self.driver.get_screenshot_as_png(), name="wipe result",
                      attachment_type=AttachmentType.PNG)
        else:
            pass

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_wipe_profile_places(self):
        self.swipe_up()
        sleep(2)
        if len(self.driver.find_elements_by_id()) > 0:
            self.go_to_show_all_profile_places()
            allure.attach(self.driver.get_screenshot_as_png(), name="initial amount",
                      attachment_type=AttachmentType.PNG)
            self.delete_all_places()
            allure.attach(self.driver.get_screenshot_as_png(), name="wipe result",
                      attachment_type=AttachmentType.PNG)
        else:
            pass

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_wipe_profile_collections(self):
        self.swipe_up()
        if len(self.driver.find_elements_by_id()) > 0:
            self.go_to_all_collections_in_profile()
            allure.attach(self.driver.get_screenshot_as_png(), name="initial amount",
                      attachment_type=AttachmentType.PNG)
            self.delete_all_collections()
            allure.attach(self.driver.get_screenshot_as_png(), name="wipe result",
                      attachment_type=AttachmentType.PNG)
        else:
            pass
