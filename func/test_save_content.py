from func.base import *


@allure.title(Title.SAVE_CONTENT.value)
class TestSaveContent(AbstractTest):

    def set_up_class(self):
        self.go_to_global_search()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_save_place_to_profile(self):
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
        common_output_block.find_elements_by_class_name('android.widget.FrameLayout')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        self.get_text_by_id('') == search_data
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        any_place = self.choose_random_profile_all_places()
        place_name = any_place.find_element_by_id('').text
        self.save_obj_longpress_to_profile(any_place)
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        saved_place = self.choose_place_by_index_profile_all_places(0)
        saved_place_name = saved_place.find_element_by_id('').text
        assert place_name == saved_place_name
        self.delete_obj_longpress(saved_place)
        sleep(2)
        try:
            self.click_element(saved_place)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_save_place_to_drafts(self):
        search_data = self.random_profile()
        self.put_text_to_input(search_data, 'searchTextField')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('recyclerGlobalSearch')
        first_search_output_block = \
        common_output_block.find_elements_by_class_name('android.widget.FrameLayout')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        self.get_text_by_id('') == search_data
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        any_place = self.choose_random_profile_all_places()
        place_name = any_place.find_element_by_id('').text
        self.save_obj_longpress_to_drafts(any_place)
        self.click_element_by_id('')
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        saved_place = self.choose_place_by_index_profile_all_places(0)
        saved_place_name = saved_place.find_element_by_id('').text
        assert place_name == saved_place_name
        self.delete_obj_longpress(saved_place)
        sleep(2)
        try:
            self.click_element(saved_place)
        except:
            EC.StaleElementReferenceException()


    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_save_place_to_drafts(self):
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('recyclerGlobalSearch')
        first_search_output_block = \
        common_output_block.find_elements_by_class_name('android.widget.FrameLayout')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id('') == search_data
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        any_col = self.choose_random_profile_collections_all()
        col_name = any_col.find_element_by_id('').text
        self.save_obj_longpress_to_drafts(any_col)
        self.click_element_by_id('')
        self.go_to_drafts_from_profile()
        self.go_to_all_collections_in_drafts()
        saved_col = self.choose_collection_by_index_profile_all_collections(0)
        saved_col_name = saved_col.find_element_by_id('').text
        assert col_name == saved_col_name
        self.delete_obj_longpress(saved_col)
        sleep(2)
        try:
            self.click_element(saved_col)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_save_place_to_drafts(self):
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
        common_output_block.find_elements_by_class_name('android.widget.FrameLayout')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id('') == search_data
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        any_col = self.choose_random_profile_collections_all()
        col_name = any_col.find_element_by_id('').text
        self.save_obj_longpress_to_profile(any_col)
        self.click_element_by_id('')
        self.go_to_all_collections_in_profile()
        saved_col = self.choose_collection_by_index_profile_all_collections(0)
        saved_col_name = saved_col.find_element_by_id('').text
        assert col_name == saved_col_name
        self.delete_obj_longpress(saved_col)
        sleep(2)
        try:
            self.click_element(saved_col)
        except:
            EC.StaleElementReferenceException()