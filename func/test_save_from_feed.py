from func.base import *

@allure.title(Title.NEWS_FEED_ACTIVITY.value)
class TestSaveFeed(AbstractTest):

    def set_up_class(self):
        self.go_to_feed()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_feed_save_place_drafts(self):
        self.scroll_down_to_id('')
        saving_name = self.get_text_by_id('')
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        poi_name = self.get_text_by_id('')
        assert saving_name == poi_name
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.go_to_drafts_from_profile()
        self.go_to_drafts_all_places()
        saved_place = self.choose_place_by_index_profile_all_places(0)
        saved_place_name = saved_place.find_element_by_id('textViewTitle').text
        assert saving_name == saved_place_name
        self.delete_obj_longpress(saved_place)
        sleep(2)
        try:
            self.click_element(saved_place)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_feed_save_col_drafts(self):
        self.scroll_down_to_id('')
        saving_name = self.get_text_by_id('')
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        poi_name = self.get_text_by_id('')
        assert saving_name == poi_name
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.go_to_drafts_from_profile()
        self.go_to_all_collections_in_drafts()
        saved_col = self.choose_collection_by_index_profile_all_collections(0)
        saved_col_name = saved_col.find_element_by_id('').text
        assert saving_name == saved_col_name
        self.delete_obj_longpress(saved_col)
        sleep(2)
        try:
            self.click_element(saved_col)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_feed_save_place_public(self):
        self.scroll_down_to_id('')
        saving_name = self.get_text_by_id('')
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        poi_name = self.get_text_by_id('')
        assert saving_name == poi_name
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.go_to_show_all_profile_places()
        saved_place = self.choose_place_by_index_profile_all_places(0)
        saved_place_name = saved_place.find_element_by_id('').text
        assert saving_name == saved_place_name
        self.delete_obj_longpress(saved_place)
        sleep(2)
        try:
            self.click_element(saved_place)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.NORMAL.value)
    def test_feed_save_col_public(self):
        self.scroll_down_to_id('')
        saving_name = self.get_text_by_id('')
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        poi_name = self.get_text_by_id('')
        assert saving_name == poi_name
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.go_to_drafts_from_profile()
        self.go_to_all_collections_in_drafts()
        saved_col = self.choose_collection_by_index_profile_all_collections(0)
        saved_col_name = saved_col.find_element_by_id('').text
        assert saving_name == saved_col_name
        self.delete_obj_longpress(saved_col)
        sleep(2)
        try:
            self.click_element(saved_col)
        except:
            EC.StaleElementReferenceException()