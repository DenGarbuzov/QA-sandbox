from func.base import *


@allure.title(Title.COLLECTION.value)
class TestEditCollection(AbstractTest):

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_edit_library(self):
        self.go_to_drafts_from_profile()
        self.popup_close_if_exist()
        self.create_global_collection()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        col.click()
        self.insect_collection_elements()
        self.click_element_by_id('')
        self.take_camera_photo_crop()
        sleep(2)
        self.not_exist_by_id('')
        self.click_element_by_id('')
        col2 = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col2)
        self.click_element_by_id('')
        text = self.random_text(50)
        self.collection_random_info_input(text)
        self.edit_content_photo_collection()
        self.random_choice_crop_use_from_library()
        self.click_element_by_id('')
        self.click_element_by_id('')
        col3 = self.choose_collection_by_index_profile_all_collections(0)
        col3_name = col3.find_element_by_id('').text
        assert col3_name == text
        self.delete_obj_longpress(col3)
        sleep(2)
        try:
            self.click_element(col2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_edit_photo(self):
        self.go_to_drafts_from_profile()
        self.popup_close_if_exist()
        self.create_global_collection()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        col.click()
        self.insect_collection_elements()
        self.click_element_by_id('')
        self.take_camera_photo_crop()
        sleep(2)
        self.not_exist_by_id('')
        self.click_element_by_id('')
        col2 = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col2)
        self.click_element_by_id('')
        text = self.random_text(50)
        self.collection_random_info_input(text)
        self.edit_content_photo_collection()
        self.take_camera_photo_crop()
        self.click_element_by_id('')
        self.click_element_by_id('')
        col3 = self.choose_collection_by_index_profile_all_collections(0)
        col3_name = col3.find_element_by_id('').text
        assert col3_name == text
        self.delete_obj_longpress(col3)
        sleep(2)
        try:
            self.click_element(col2)
        except:
            EC.StaleElementReferenceException()
