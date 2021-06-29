from func.base import *

@allure.title(Title.MAIN_ACTIVITY.value)
class TestLanguageChange(AbstractTest):

    """
       работает согласно новой логике, требуется ID кнопок "английский", "русский"

       """
    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.MINER.value)
    def test_change_language(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="language fix",
                      attachment_type=AttachmentType.PNG)
        button_text1 = self.get_text_by_id('')
        button_text2 = self.get_text_by_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')

        self.wait_by_id('', 15)
        if button_text1 == '':
            main_block = self.driver.find_element_by_id('')
            language_block = main_block.find_element_by_id('')
            button_block = language_block.find_element_by_class_name('')
            button_english = button_block.find_elements_by_class_name('')
            button_english[1].click()
        else:
            main_block = self.driver.find_element_by_id('')
            language_block = main_block.find_element_by_id('')
            button_block = language_block.find_element_by_class_name('')
            button_russian = button_block.find_elements_by_class_name('')
            button_russian[2].click()

        allure.attach(self.driver.get_screenshot_as_png(), name="sigh in language view",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        button_text3 = self.get_text_by_id('')
        button_text4 = self.get_text_by_id('')
        assert button_text1 != button_text3
        assert button_text2 != button_text4
        allure.attach(self.driver.get_screenshot_as_png(), name="profile state",
                      attachment_type=AttachmentType.PNG)