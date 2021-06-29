from func.base import *


@allure.title(Title.PROD_TEST.value)
class TestCreatingCollectionGlobal(AbstractTest):
    """
    Переделать согласно уточненной логике'
    """

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_create_global_drafts_photo(self):
        self.go_to_drafts_from_profile()
        self.create_global_collection()
        self.popup_close_if_exist()
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
        self.delete_obj_longpress(col2)
        sleep(2)
        try:
            self.click_element(col2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_create_global_drafts_library(self):
        self.go_to_drafts_from_profile()
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        col.click()
        self.insect_collection_elements()
        self.click_element_by_id('')
        self.random_choice_crop_use_from_library()
        sleep(2)
        self.not_exist_by_id('')
        self.click_element_by_id('')
        col2 = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col2)
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        sleep(2)
        try:
            self.click_element(col2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_create_global_public_photo(self):
        self.create_global_collection()
        self.popup_close_if_exist()
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
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        sleep(2)
        try:
            self.click_element(col2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_create_global_public_library(self):
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        col.click()
        self.insect_collection_elements()
        self.click_element_by_id('')
        self.random_choice_crop_use_from_library()
        sleep(2)
        self.not_exist_by_id('')
        self.click_element_by_id('')
        col2 = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col2)
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        sleep(2)
        try:
            self.click_element(col2)
        except:
            EC.StaleElementReferenceException()
