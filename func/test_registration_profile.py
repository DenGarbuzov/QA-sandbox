from func.base import *


@allure.title(Title.MAIN_ACTIVITY.value)
class Test_profile_registration(AbstractTest):

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.BLOCKER.value)
    def test_registration_new_user(self):
        self.go_to_profile_options()
        self.log_out_from_options()
        self.click_element_by_id('')
        word = ''
        random_login = word.join(
            random.choice(string.ascii_lowercase + string.digits) for x in range(5))
        self.generate_and_past_mail_login_password(random_login)
        allure.attach(self.driver.get_screenshot_as_png(), name="new profile info",
                      attachment_type=AttachmentType.PNG)
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        assert self.get_text_by_id('') == random_login
