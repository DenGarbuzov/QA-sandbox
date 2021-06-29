from func.base import *


@allure.title(Title.COLLECTION.value)
class TestCollectionContentActions(AbstractTest):

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_adding_place_collection_drafts(self):
        self.go_to_drafts_from_profile()
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col)
        self.click_element_by_id('')
        text = self.random_text(30)
        self.put_text_to_input(text,)
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_global_search('')
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        sleep(3)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
            common_output_block.find_elements_by_class_name()[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id() == search_data
        self.scroll_down_to_id()
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        any_place = self.choose_random_profile_all_places()
        place_name = any_place.find_element_by_id('').text
        self.save_obj_longpress_to_drafts(any_place)
        self.click_element_by_id('')
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.go_to_drafts_all_places()
        saved_place = self.choose_place_by_index_profile_all_places(0)
        saved_place_name = saved_place.find_element_by_id('').text
        assert place_name == saved_place_name
        self.long_press_obj(saved_place)
        self.click_element_by_id('')
        sleep(2)
        self.wait_by_id('',15)
        self.put_text_to_input(text,'')
        self.wait_by_id('',15)
        assert self.get_text_by_id('') == text
        sleep(1)
        self.click_element_by_id('')
        sleep(1)
        self.click_element_by_id('')
        sleep(1)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        sleep(1)
        main_collection = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        assert main_collection
        col_card = main_collection.parent.find_element_by_id('')
        allure.attach(self.driver.get_screenshot_as_png(), name="collection adding to",
                      attachment_type=AttachmentType.PNG)
        col_card.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 10)
        saved_place_in_collection = self.choose_place_by_index_profile_all_places(0)
        saved_place_name_in_collection = saved_place_in_collection.find_element_by_id('').text
        assert place_name == saved_place_name_in_collection
        assert len(self.driver.find_elements_by_id('')) == 1
        self.click_element_by_id('')
        self.click_element_by_id('')
        last_event_col = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        col_card2 = last_event_col.parent.find_element_by_id('')
        self.delete_obj_longpress(col_card2)
        sleep(2)
        try:
            self.click_element(col_card2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_add_collection_drafts(self):
        self.go_to_drafts_from_profile()
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col)
        self.click_element_by_id('')
        text = self.random_text(30)
        self.put_text_to_input(text, '')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_global_search()
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('recyclerGlobalSearch', 15)
        sleep(3)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
            common_output_block.find_elements_by_class_name('')[0]
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
        self.long_press_obj(saved_col)
        self.click_element_by_id('')
        sleep(2)
        self.wait_by_id('', 15)
        self.put_text_to_input(text, '')
        self.wait_by_id('', 15)
        assert self.get_text_by_id('') == text
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        sleep(2)
        main_collection = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        assert main_collection
        col_card = main_collection.parent.find_element_by_id('')
        col_card.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('',10)
        saved_col_in_col = self.choose_collection_by_index_profile_all_collections(0)
        saved_col_name_in_col = saved_col_in_col.find_element_by_id('').text
        assert saved_col_name_in_col == saved_col_name
        assert len(self.driver.find_elements_by_id('')) == 1
        self.click_element_by_id('')
        self.click_element_by_id('')
        last_event_col = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        col_card2 = last_event_col.parent.find_element_by_id('')
        self.delete_obj_longpress(col_card2)
        sleep(2)
        try:
            self.click_element(col_card2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_delete_place_collection_drafts(self):
        self.go_to_drafts_from_profile()
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col)
        self.click_element_by_id('')
        text = self.random_text(30)
        self.put_text_to_input(text,'')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_global_search()
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        sleep(3)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
            common_output_block.find_elements_by_class_name('')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id('') == search_data
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        any_place = self.choose_random_profile_all_places()
        place_name = any_place.find_element_by_id('').text
        self.save_obj_longpress_to_drafts(any_place)
        self.click_element_by_id('')
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.go_to_drafts_all_places()
        saved_place = self.choose_place_by_index_profile_all_places(0)
        saved_place_name = saved_place.find_element_by_id('').text
        assert place_name == saved_place_name
        self.long_press_obj(saved_place)
        self.click_element_by_id('')
        sleep(2)
        self.wait_by_id('',15)
        self.put_text_to_input(text,'')
        self.wait_by_id('',15)
        assert self.get_text_by_id('') == text
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        sleep(2)
        main_collection = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        assert main_collection
        col_card = main_collection.parent.find_element_by_id('')
        col_card.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 10)
        saved_place_in_collection = self.choose_place_by_index_profile_all_places(0)
        saved_place_name_in_collection = saved_place_in_collection.find_element_by_id('').text
        assert place_name == saved_place_name_in_collection
        assert len(self.driver.find_elements_by_id('')) == 1
        self.delete_obj_longpress(saved_place_in_collection)
        assert len(self.driver.find_elements_by_id('')) == 0
        self.click_element_by_id('')
        self.click_element_by_id('')
        last_event_col = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        col_card2 = last_event_col.parent.find_element_by_id('')
        self.delete_obj_longpress(col_card2)
        sleep(2)
        try:
            self.click_element(col_card2)
        except:
            EC.StaleElementReferenceException()


    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_delete_collection_drafts(self):
        self.go_to_drafts_from_profile()
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col)
        self.click_element_by_id('')
        text = self.random_text(30)
        self.put_text_to_input(text, '')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_global_search()
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        self.wait_by_id('', 15)
        sleep(3)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
            common_output_block.find_elements_by_class_name('')[0]
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
        self.long_press_obj(saved_col)
        self.click_element_by_id('')
        sleep(2)
        self.wait_by_id('', 15)
        self.put_text_to_input(text, '')
        self.wait_by_id('', 15)
        assert self.get_text_by_id('') == text
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        sleep(2)
        main_collection = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        assert main_collection
        col_card = main_collection.parent.find_element_by_id('')
        col_card.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('',10)
        saved_col_in_col = self.choose_collection_by_index_profile_all_collections(0)
        saved_col_name_in_col = saved_col_in_col.find_element_by_id('').text
        assert len(self.driver.find_elements_by_id('')) == 1
        assert saved_col_name_in_col == saved_col_name
        self.delete_obj_longpress(saved_col_in_col)
        assert len(self.driver.find_elements_by_id('')) == 0
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(1)
        last_event_col = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        col_card2 = last_event_col.parent.find_element_by_id('')
        self.delete_obj_longpress(col_card2)
        sleep(2)
        try:
            self.click_element(col_card2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_delete_place_collection_profile(self):
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col)
        self.click_element_by_id('')
        text = self.random_text(30)
        self.put_text_to_input(text,'')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_global_search()
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        sleep(3)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
            common_output_block.find_elements_by_class_name('')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id('') == search_data
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
        self.long_press_obj(saved_place)
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)
        self.wait_by_id('',15)
        self.put_text_to_input(text,'')
        self.wait_by_id('',15)
        assert self.get_text_by_id('') == text
        self.driver.hide_keyboard()
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        sleep(2)
        main_collection = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        assert main_collection
        col_card = main_collection.parent.find_element_by_id('')
        col_card.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 10)
        saved_place_in_collection = self.choose_place_by_index_profile_all_places(0)
        saved_place_name_in_collection = saved_place_in_collection.find_element_by_id('').text
        assert place_name == saved_place_name_in_collection
        assert len(self.driver.find_elements_by_id('')) == 1
        self.delete_obj_longpress(saved_place_in_collection)
        assert len(self.driver.find_elements_by_id('')) == 0
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 10)
        last_event_col = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        col_card2 = last_event_col.parent.find_element_by_id('')
        self.delete_obj_longpress(col_card2)
        sleep(2)
        try:
            self.click_element(col_card2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_delete_collection_profile(self):
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col)
        self.click_element_by_id('')
        text = self.random_text(30)
        self.put_text_to_input(text, '')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_global_search()
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                          attachment_type=AttachmentType.PNG)
        sleep(1)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
                common_output_block.find_elements_by_class_name('')[0]
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
        self.long_press_obj(saved_col)
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)
        self.wait_by_id('', 15)
        self.put_text_to_input(text, '')
        self.wait_by_id('', 15)
        assert self.get_text_by_id('') == text
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        sleep(2)
        main_collection = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        assert main_collection
        col_card = main_collection.parent.find_element_by_id('')
        col_card.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 10)
        saved_col_in_col = self.choose_collection_by_index_profile_all_collections(0)
        saved_col_name_in_col = saved_col_in_col.find_element_by_id('').text
        assert len(self.driver.find_elements_by_id('')) == 1
        assert saved_col_name_in_col == saved_col_name
        self.delete_obj_longpress(saved_col_in_col)
        assert len(self.driver.find_elements_by_id('')) == 0
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(1)
        last_event_col = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        col_card2 = last_event_col.parent.find_element_by_id('')
        self.delete_obj_longpress(col_card2)
        sleep(2)
        try:
            self.click_element(col_card2)
        except:
            EC.StaleElementReferenceException()

    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('С')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_collection_delete_collection_profile(self):
        self.create_global_collection()
        self.popup_close_if_exist()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col)
        self.click_element_by_id('')
        text = self.random_text(30)
        self.put_text_to_input(text, '')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_global_search()
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                          attachment_type=AttachmentType.PNG)
        sleep(1)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
                common_output_block.find_elements_by_class_name('')[0]
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
        self.long_press_obj(saved_col)
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)
        self.wait_by_id('', 15)
        self.put_text_to_input(text, '')
        self.wait_by_id('', 15)
        assert self.get_text_by_id('') == text
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        sleep(2)
        main_collection = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        assert main_collection
        col_card = main_collection.parent.find_element_by_id('')
        col_card.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 10)
        saved_col_in_col = self.choose_collection_by_index_profile_all_collections(0)
        saved_col_name_in_col = saved_col_in_col.find_element_by_id('').text
        assert len(self.driver.find_elements_by_id('')) == 1
        assert saved_col_name_in_col == saved_col_name
        # self.delete_obj_longpress(saved_col_in_col)
        # assert len(self.driver.find_elements_by_id('collectionCard')) == 0
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(1)
        last_event_col = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        col_card2 = last_event_col.parent.find_element_by_id('')
        self.disband_col_longpress(col_card2)
        sleep(2)
        try:
            self.click_element(col_card2)
        except:
            EC.StaleElementReferenceException()
        disband_col = self.driver.find_element_by_xpath("//*[@text='" + saved_col_name + "']")
        col2_card = disband_col.parent.find_element_by_id('')
        self.delete_obj_longpress(col2_card)
        sleep(2)
        try:
            self.click_element(col2_card)
        except:
            EC.StaleElementReferenceException()


    @allure.feature(Feature.FUNC_TEST.value)
    @allure.story('')
    @allure.severity(severity_level=Level.CRITICAL.value)
    def test_disband_collection_drafts(self):
        self.go_to_drafts_from_profile()
        self.popup_close_if_exist()
        self.create_global_collection()
        self.go_to_all_collections_in_profile()
        col = self.choose_collection_by_index_profile_all_collections(0)
        self.long_press_obj(col)
        self.click_element_by_id('')
        text = self.random_text(30)
        self.put_text_to_input(text,'')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.go_to_global_search()
        search_data = self.random_profile()
        self.put_text_to_input(search_data, '')
        allure.attach(self.driver.get_screenshot_as_png(), name="searching text",
                      attachment_type=AttachmentType.PNG)
        sleep(3)
        self.wait_by_id('', 15)
        common_output_block = self.driver.find_element_by_id('')
        first_search_output_block = \
            common_output_block.find_elements_by_class_name('')[0]
        first_search_output_block.click()
        self.wait_by_id('', 15)
        allure.attach(self.driver.get_screenshot_as_png(), name="output result",
                      attachment_type=AttachmentType.PNG)
        assert self.get_text_by_id('') == search_data
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        any_place = self.choose_random_profile_all_places()
        place_name = any_place.find_element_by_id('').text
        self.save_obj_longpress_to_drafts(any_place)
        self.click_element_by_id('')
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.go_to_drafts_all_places()
        saved_place = self.choose_place_by_index_profile_all_places(0)
        saved_place_name = saved_place.find_element_by_id('').text
        assert place_name == saved_place_name
        self.long_press_obj(saved_place)
        self.click_element_by_id('')
        sleep(2)
        self.wait_by_id('',15)
        self.put_text_to_input(text,'')
        self.wait_by_id('',15)
        assert self.get_text_by_id('') == text
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        self.click_element_by_id('')
        sleep(2)
        main_collection = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        assert main_collection
        col_card = main_collection.parent.find_element_by_id('')
        col_card.click()
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 10)
        saved_place_in_collection = self.choose_place_by_index_profile_all_places(0)
        saved_place_name_in_collection = saved_place_in_collection.find_element_by_id('').text
        assert place_name == saved_place_name_in_collection
        assert len(self.driver.find_elements_by_id('')) == 1
        self.click_element_by_id('')
        self.click_element_by_id('')
        last_event_col = self.driver.find_element_by_xpath("//*[@text='" + text + "']")
        col_card2 = last_event_col.parent.find_element_by_id('')
        self.disband_col_longpress(col_card2)
        try:
            self.click_element(col_card2)
        except:
            EC.StaleElementReferenceException()
        sleep(2)
        self.click_element_by_id('')
        self.scroll_up_to_id('')
        self.click_element_by_id('')
        dis_place = self.choose_place_by_index_profile_all_places(0)
        dis_place_name = dis_place.find_element_by_id('').text
        assert dis_place_name == saved_place_name
        self.delete_obj_longpress(dis_place)
        try:
            self.click_element(dis_place)
        except:
            EC.StaleElementReferenceException()