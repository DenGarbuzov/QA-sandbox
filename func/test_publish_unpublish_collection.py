from func.base import *


@allure.title(Title.PROD_TEST.value)
class TestPublishUnpublishCollection(AbstractTest):
    """
    Переделать согласно уточненной логике'
    """

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story(' ')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_publish_from_drafts(self):
        self.go_to_drafts_from_profile()
        self.create_global_collection()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        col.click()
        self.insect_collection_elements()
        sleep(2)
        self.click_element_by_id('')
        col2 = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col2)
        self.click_element_by_id('')
        text = self.random_text(10)
        self.collection_random_info_input(text)
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(1)
        col3 = self.choose_collection_by_index_profile_all_collections(0)
        col3_name = col3.find_element_by_id('').text
        assert col3_name == text
        self.long_press_options_col_publish_click(col3)
        sleep(2)
        self.click_element_by_id('')
        self.go_to_all_collections_in_profile()
        self.wait_by_id('', 15)
        col4 = self.choose_collection_by_index_profile_all_collections(0)
        col4_name = col4.find_element_by_id('').text
        assert col4_name == text
        self.delete_obj_longpress(col4)
        try:
            self.click_element(col4)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story(' ')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_unpublish_from_public(self):
        self.create_global_collection()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        col.click()
        self.insect_collection_elements()
        sleep(2)
        self.click_element_by_id('')
        col2 = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col2)
        self.click_element_by_id('')
        text = self.random_text(10)
        self.collection_random_info_input(text)
        self.click_element_by_id('')
        self.click_element_by_id('')
        col3 = self.choose_collection_by_index_profile_all_collections(0)
        col3_name = col3.find_element_by_id('').text
        assert col3_name == text
        self.long_press_options_col_unpublish_click(col3)
        sleep(2)
        self.click_element_by_id('')
        self.go_to_drafts_from_profile()
        self.go_to_all_collections_in_drafts()
        self.wait_by_id('', 15)
        col4 = self.choose_collection_by_index_profile_all_collections(0)
        col4_name = col4.find_element_by_id('').text
        assert col4_name == text
        self.delete_obj_longpress(col4)
        try:
            self.click_element(col4)
        except:
            EC.StaleElementReferenceException()