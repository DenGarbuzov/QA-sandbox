import enum
import uuid
from abc import abstractmethod
from enum import Enum
import random
from time import sleep
import allure
import pytest
import string

from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@enum.unique
class Title(Enum):
    MAIN_ACTIVITY = ''
    MAP_ACTIVITY = ''
    PLACE_ACTIVITY = ''
    NEWS_FEED_ACTIVITY = ''
    COLLECTION = ''
    DRAFTS = ''
    PROD_TEST = ''
    BACKGROUND = ''
    GLOBAL_SEARCH = ''
    SAVE_CONTENT = ''


@enum.unique
class Feature(Enum):
    CLICK_ELEMENT = ''
    CHECK_EXIST_ELEMENT = ''
    FUNC_TEST = ''


@enum.unique
class Level(Enum):
    """
    По убыванию - в зависимости от важности
    """
    BLOCKER = 'blocker'
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINER = 'miner'
    TRIVIAL = 'trivial'


@pytest.mark.usefixtures('driver', 'set_up')
class AbstractTest(object):
    driver: webdriver = None

    @pytest.fixture()
    def set_up(self):
        self.set_up_class()

    @abstractmethod
    def set_up_class(self):
        pass

    @staticmethod
    def about_profile_main_text():
        text = ''
        return text

    def about_profile_block(self):
        self.wait_by_id('', 15)
        main_block = self.driver.find_element_by_id('')
        main_block_child = main_block.find_element_by_class_name('')
        about_profile_block = main_block_child.find_element_by_id('')
        return about_profile_block

    def activate_option_button(self):
        options = self.driver.find_element_by_id('')
        assert options
        assert options.click

    def assert_adding_photo_in_all_photo_place_view(self):
        all_photo_blocks = self.driver.find_element_by_id('')
        individual_photo_block = all_photo_blocks.find_elements_by_class_name(
            '')
        assert len(individual_photo_block) > 1

    def background_set(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)

    def back_to_options_from_lower_layer(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        sleep(3)
        self.confirm_options_location()

    def back_from_options_to_profile(self):
        self.is_exist_by_element_id('')
        self.click_element_by_id('')
        self.confirm_profile_page()

    def category_random_chose_creating_place(self):
        self.wait_by_id('', 15)
        # assert self.get_text_by_id('selectCategoryButton') == 'КАТЕГОРИЯ'
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        all_categories = self.driver.find_elements_by_class_name('')
        cat = random.choice(tuple(all_categories))
        cat.click()
        cat.get_attribute('') == ''
        cat_name_local = self.get_text_by_obj(cat)
        self.driver.press_keycode(4)
        cat_name_global = self.get_text_by_id('')
        assert cat_name_local == cat_name_global

    def click_element_by_id(self, element_id: str) -> bool:
        allure.step('Нажатие на элемент - id : {}'.format(element_id))
        self.wait_by_id(element_id, 15)
        button = self.driver.find_element_by_id(element_id)
        if button and button.is_enabled():
            button.click()
            return True
        return False

    def check_avatar_options(self):

        if len(self.driver.find_elements_by_id('')) > 0:
            self.is_exist_by_element_id('')
            self.is_exist_by_element_id('')

        else:
            self.is_exist_by_element_id('')
            self.is_exist_by_element_id('')


    def click_done_options_done_button(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)

    def choose_place_by_index_profile_all_places(self, index=list):
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        main_block = self.driver.find_element_by_id('')
        second_layer = main_block.find_element_by_id('')
        places_list = second_layer.find_elements_by_id('')
        chosen_place = places_list[index]
        return chosen_place

    def choose_collection_by_index_profile_all_collections(self, index=list):
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        all_collections = self.driver.find_elements_by_id('')
        chosen_collection = all_collections[index]
        return chosen_collection

    def insect_collection_elements(self):
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)

    def choose_place_by_index_profile_places(self, index=list):
        self.wait_by_id('', 15)
        main_block = self.driver.find_element_by_id('')
        places_list = main_block.find_elements_by_id('')
        chosen_place = places_list[index]
        return chosen_place

    def choose_random_profile_all_places(self):
        self.wait_by_id('', 10)
        main_block = self.driver.find_element_by_id('')
        places_list = main_block.find_elements_by_id('')
        del places_list[-4:]
        chosen_place = random.choice(tuple(places_list))
        return chosen_place

    def choose_random_profile_places(self):
        self.wait_by_id('', 10)
        main_block = self.driver.find_element_by_id('')
        places_list = main_block.find_elements_by_id('')
        del places_list[-4:]
        chosen_place = random.choice(tuple(places_list))
        return chosen_place

    def choose_random_profile_collections_all(self):
        self.wait_by_id('',15)
        all_collections = self.driver.find_elements_by_id('')
        choosen_collection = random.choice(tuple(all_collections))
        return choosen_collection

    def click_element(self, element) -> bool:
        allure.step('Нажатие на элемент - id : {}'.format(element))
        self.wait_element(element, 15)
        button = self.driver.find_element(element)
        if button and button.is_enabled():
            button.click()
            return True
        return False

    def confirm_profile_page(self):
        assert self.is_exist_by_element_id('')
        assert self.is_exist_by_element_id('')
        assert self.is_exist_by_element_id('')

    def collection_random_info_input(self, text):
        self.wait_by_id('', 15)
        self.put_text_to_input(text, '')
        description_text = self.random_text(2000)
        self.click_element_by_id('')
        self.put_text_to_input(description_text, '')
        self.driver.hide_keyboard()
        self.driver.press_keycode(4)
        self.wait_by_id('', 15)

    def click_element_by_class(self, element_class: str) -> bool:
        allure.step('Нажатие на элемент - class : {}'.format(element_class))
        self.wait_by_class(element_class, 20)
        button = self.driver.resource - id(element_class)
        if button and button.is_enabled():
            button.click()
            return True
        return False

    def click_register_button_after_input(self):
        allure.step('')
        register_button = self.click_element_by_id('')
        self.wait_by_id('', 2)
        assert register_button

    def click_element_by_class_name(self, element_class_name: str) -> bool:
        allure.step('Нажатие на элемент - class name : {}'.format(element_class_name))
        self.wait_by_id(element_class_name, 20)
        button = self.driver.find_element_by_class_name(element_class_name)
        if button and button.is_enabled():
            button.click()
            return True
        return False

    def check_profile_photo_content(self):
        assert self.is_exist_by_element_id('')
        assert self.is_exist_by_element_id('')
        assert self.is_exist_by_element_id('')

    def create_place_copy(self, index=int) -> None:  # выбор 0 - ОТМЕНА, 1 - СОЗДАТЬ КОПИЮ:
        but_panel = self.driver.find_element_by_id('')
        inner_layer_but_panel = but_panel.find_element_by_class_name('')
        buttons = inner_layer_but_panel.find_elements_by_class_name('')
        buttons[0].text == ''
        buttons[1].text == ' '
        text_block = self.driver.find_element_by_id('')
        inner_layer_text_block = text_block.find_element_by_class_name('.widget.ScrollView')
        info = inner_layer_text_block.find_element_by_class_name('.widget.LinearLayout')
        info_text = info.find_element_by_id('android:id/')
        info_text.text == '?'
        buttons[index].click()
        sleep(5)

    def create_global_collection(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.click_element_by_id('')

    def change_password(self, old_pass=str, new_pass=str, confirm_new_pass=str):
        main_layer = self.driver.find_element_by_id('')
        input_fields = main_layer.find_elements_by_id('')
        allure.step('')
        self.put_text_to_input_obj(old_pass, input_fields[0])
        allure.step('')
        self.put_text_to_input_obj(new_pass, input_fields[1])
        allure.step('')
        self.put_text_to_input_obj(confirm_new_pass, input_fields[2])
        save_button = self.driver.find_element_by_id('')
        save_button.click()
        self.wait_by_id('', 15)
        sleep(5)

    def confirm_options_location(self):
        self.wait_by_id('', 15)
        assert self.get_text_by_id('') == ''
        sleep(3)

    def confirm_main_screen(self):
        self.is_exist_by_element_id('')
        self.is_exist_by_element_id('')
        self.is_exist_by_element_id('')
        self.is_exist_by_element_id('')

    def confirm_auth_screen(self):
        self.is_exist_by_element_id('')
        self.is_exist_by_element_id('')
        self.is_exist_by_element_id('')

    def delete_all_places(self):
        self.wait_by_id('', 5)
        while len(self.driver.find_elements_by_id('')) > 0:
            place = self.choose_place_by_index_profile_all_places(0)
            self.delete_obj_longpress(place)
        else:
            assert len(self.driver.find_elements_by_id('')) == 0

    def delete_all_collections(self):
        self.wait_by_id('', 5)
        while len(self.driver.find_elements_by_id('')) > 0:
            collection = self.choose_collection_by_index_profile_all_collections(0)
            self.delete_obj_longpress(collection)
        else:
            assert len(self.driver.find_elements_by_id('')) == 0

    def delete_menu_delete_click(self, index=int):  # 0-ОТМЕНА, 1-ПРОДОЛЖИТЬ
        self.driver.find_element_by_id('')
        but_panel = self.driver.find_element_by_id('')
        inner_layer_but_panel = but_panel.find_element_by_class_name('')
        buttons = inner_layer_but_panel.find_elements_by_class_name('')
        buttons[0].text == ''
        buttons[1].text == ''
        text_block = self.driver.find_element_by_id('')
        inner_layer_text_block = text_block.find_element_by_class_name('')
        info = inner_layer_text_block.find_element_by_class_name('')
        info_text = info.find_element_by_id('android:id/')
        info_text.text == ''
        buttons[index].click()
        sleep(5)

    def delete_background(self):
        if not self.is_exist_by_element_id(''):
            self.click_element_by_id('')
            sleep(2)
            allure.step('')
            self.click_element_by_id('')
            sleep(2)
            assert self.is_exist_by_element_id('')
        else:
            pass

    def delete_obj_longpress(self, element):
        self.long_press_obj(element)
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)

    def disband_col_longpress(self, element):
        self.long_press_obj(element)
        self.click_element_by_id('')
        sleep(2)

    def delete_avatar_profile(self):
        while self.not_exist_by_id(''):
            self.click_element_by_id('')
            self.wait_by_id('', 15)
            self.click_element_by_id('')
            sleep(2)
        else:
            pass

    def delete_avatar_profile_by_edit_if_set(self):
        if len(self.driver.find_elements_by_id('')) > 0:
            self.click_element_by_id('')
            self.click_element_by_id('')
            self.is_exist_by_element_id('')
            self.is_exist_by_element_id('')
            self.driver.press_keycode(4)
            self.click_element_by_id('')
            self.click_element_by_id('')
        else:
            pass

    def delete_avatar_using_options(self):
        self.click_element_by_id('')
        sleep(2)
        self.click_element_by_id('')
        sleep(2)
        allure.step('')
        assert self.click_element_by_id('')

    def delete_avatar_if_set(self):
        self.click_element_by_id('')
        a = self.driver.find_elements_by_id('')
        if len(a) >= 1:
            self.click_element_by_id('')
            sleep(2)
        else:
            self.driver.press_keycode(4)

    def delete_background_if_set(self):
        self.click_element_by_id('')
        delete_button = self.driver.find_elements_by_id('')
        if len(delete_button) >= 1:
            self.click_element_by_id('')
            sleep(3)
        else:
            self.driver.press_keycode(4)

    def edit_content_photo_collection(self):
        self.click_element_by_id('')
        self.click_element_by_id('')

    def edit_content_photo_place(self):
        self.click_element_by_id('')
        self.click_element_by_id('')

    def go_to_global_search(self):
        self.click_element_by_id('')
        self.wait_by_id('', 15)

    def go_to_checkin(self):
        self.wait_by_id('', 10)
        assert self.driver.find_element_by_id('')
        button = self.driver.find_element_by_id('')
        button.click()
        self.wait_by_id('', 10)

    def go_to_feed(self):
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)

    def go_to_show_all_profile_places(self):
        self.scroll_down_to_id('')
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 10)

    def geo_random_text_pre_config_without_photo(self, text):
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        sleep(2)
        self.tap_create_poi_marker()
        self.wait_by_id('', 15)
        self.put_text_to_input(text, '')
        self.click_element_by_id('')
        description_text = self.random_text(250)
        self.put_text_to_input(description_text, '')
        self.driver.hide_keyboard()
        self.driver.press_keycode(4)

    def tap_by_coordinates(self, x, y, z):
        actions = TouchAction(self.driver)
        actions.tap(None, x, y, count=z)
        actions.perform()

    def tap_create_poi_marker(self):
        # self.tap_by_coordinates(735, 960, 1)
        # self.tap_centre_screen(1)
        self.driver.switch_to.context('WEBVIEW_com.')
        self.driver.find_element_by_xpath("//*[@id='']").click()
        self.driver.switch_to.context('NATIVE_APP')



    def tap_centre_screen(self, z):
        size = self.driver.get_window_size()
        # Screen width width
        x = size['width']
        # The height of the screen height
        y = size['height']
        x1 = x * 0.5
        y1 = y * 0.4
        print(x1, y1)
        actions = TouchAction(self.driver)
        actions.tap(None, x1, y1, count=z)
        actions.perform()

    def tap_enter_button_prop_screen(self, z):
        size = self.driver.get_window_size()
        # Screen width width
        x = size['width']
        # The height of the screen height
        y = size['height']
        x1 = x * 0.93
        y1 = y * 0.96
        print(x1, y1)
        actions = TouchAction(self.driver)
        actions.tap(None, x1, y1, count=z)
        actions.perform()

    def get_text_by_id(self, element_id: str) -> str:
        element = self.driver.find_element_by_id(element_id)
        assert element
        return element.text

    def get_text_by_obj(self, element) -> str:
        assert element
        return element.text

    def go_to_edit_profile(self):
        self.wait_by_id('editButton', 15)
        self.get_text_by_id('') == ''
        self.click_element_by_id('')
        self.is_exist_by_element_id('')
        self.get_text_by_id('') == ''

    def go_to_profile(self):
        self.wait_by_id('', 15)
        allure.step('')
        profile_icon = self.driver.find_element_by_id('')
        assert profile_icon
        assert profile_icon.is_enabled()
        profile_icon.click()
        sleep(3)

    def go_to_change_profile_password(self):
        self.wait_by_id('', 15)
        ch_pass_button = self.driver.find_element_by_id('')
        assert ch_pass_button
        ch_pass_button.click()

    def go_to_blocked_profiles(self):
        self.wait_by_id('', 15)
        blocked_pr_button = self.driver.find_element_by_id('')
        assert blocked_pr_button
        blocked_pr_button.click()

    def go_to_drafts_from_profile(self):
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)

    def go_to_drafts_all_places(self):
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)

    def go_to_all_collections_in_profile(self):
        self.scroll_down_to_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)

    def go_to_all_collections_in_drafts(self):
        self.click_element_by_id('')
        self.is_exist_by_element_id('')

    def go_to_profile_options(self):
        allure.step('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)

    def generate_and_past_mail_login_password(self, random_login):
        allure.step(
            'Генерация случайной почты, логина и пароля состоящего из букв английского алфавита'
            'и цифр от 0 до 9')
        word = ''
        mail = word.join(
            random.choice(string.ascii_lowercase + string.digits) for x in range(5)) + '@gmail.com'
        password = word.join(
            random.choice(string.ascii_lowercase + string.digits) for x in range(8))
        allure.step('Ввод почты, логина и пароля в соответствующие поля')
        text_field = self.driver.find_elements_by_id('')
        self.put_text_to_input_obj(random_login, text_field[0])
        self.put_text_to_input_obj(mail, text_field[1])
        self.put_text_to_input_obj(password, text_field[2])

    def go_to_bug_report(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')

    def profile_name(self):
        self.wait_by_id('', 15)
        name = self.get_text_by_id('')
        return name

    def long_press_by_id(self, id=str):
        actions = TouchAction(self.driver)
        a = self.driver.find_element_by_id(id)
        actions.long_press(a, duration=3000)
        actions.perform()

    def tap_by_id(self, element: str):
        actions = TouchAction(self.driver)
        actions.tap(element)
        actions.perform()

    def profile_edit_login(self, new_login=str):
        login_block = self.driver.find_element_by_id('')
        child_login_block = login_block.find_element_by_class_name('')
        edit_login_text = child_login_block.find_element_by_id('')
        self.put_text_to_input_obj(new_login, edit_login_text)
        self.click_element_by_id('')
        assert self.get_text_by_obj(edit_login_text) == new_login

    @staticmethod
    def random_text(n: int):
        res = ''.join(
            random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=n))
        return str(res)

    def name_profile_block(self):
        login_block = self.driver.find_element_by_id('')
        child_login_block = login_block.find_element_by_class_name('')
        edit_name_text = child_login_block.find_element_by_id('')
        return edit_name_text

    def place_content_edit(self, text):
        self.wait_by_id('', 15)
        self.put_text_to_input(text, '')
        self.click_element_by_id('')
        description_text = self.random_text(4000)
        self.put_text_to_input(description_text, '')
        self.driver.hide_keyboard()
        self.driver.press_keycode(4)

    def popup_close_if_exist(self):
        sleep(5)
        if len(self.driver.find_elements_by_id('')) > 0:
            self.click_element_by_id('')
        else:
            try:
                self.driver.find_element_by_id('')
            except:
                EC.StaleElementReferenceException()

    def get_screen_size(self):
        size = self.driver.get_window_size()
        # Screen width width
        x = size['width']
        # The height of the screen height
        y = size['height']
        print(size)
        return x and y

    def put_random_text_to_about_profile_block(self, n=int):
        about_text_area = self.about_profile_block()
        input_text = self.random_text(n)
        self.put_text_no_clear_to_element_input(input_text, about_text_area)
        self.click_element_by_id('')
        sleep(10)

    def put_text_to_input_obj(self, text, object):
        input_text: WebElement = object
        input_text.clear()
        input_text.send_keys(text)

    def login_profile_block(self):
        login_block = self.driver.find_element_by_id('')
        child_login_block = login_block.find_element_by_class_name('..')
        edit_login_text = child_login_block.find_element_by_id('')
        return edit_login_text

    def long_press_obj(self, element):
        actions = TouchAction(self.driver)
        actions.long_press(element)
        actions.perform()

    def log_out_from_options(self):
        self.wait_by_id('', 15)
        self.click_element_by_id('')
        self.wait_by_id('android:id', 15)
        self.click_element_by_id('')
        self.wait_by_id('', 15)

    def move_object_to(self, element1, element2):
        actions = TouchAction(self.driver)
        actions.long_press(element1).move_to(element2).wait(500).release()
        actions.perform()

    def tap_obj(self, element):
        actions = TouchAction(self.driver)
        actions.tap(element)
        actions.perform()

    def profile_place_options_long_press(self):
        self.scroll_to_id('')
        places_block = self.driver.find_element_by_id('')
        places_list = places_block.find_elements_by_id('')
        elem = places_list[0]
        self.swipe_up()
        self.long_press_obj(elem)
        sleep(5)

    def save_obj_longpress(self, element):
        self.long_press_obj(element)
        self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)

    def save_obj_longpress_to_drafts(self, element):
        self.long_press_obj(element)
        self.click_element_by_id('')
        self.click_element_by_id('')

    def save_obj_longpress_to_profile(self, element):
        self.long_press_obj(element)
        self.click_element_by_id('')
        self.click_element_by_id('')

    def scroll_down_to_id(self, id=str):
        while self.not_exist_by_id(id):
            self.swipe_up_screen()
        else:
            pass
        self.is_exist_by_element_id(id)

    def scroll_up_to_id(self, id=str):
        while self.not_exist_by_id(id):
            self.swipe_down_screen()
        else:
            self.wait_by_id(id, 15)
            pass
        self.is_exist_by_element_id(id)

    def search_by_name(self, name=str):
        self.driver.MobileBy.ACCESSIBILITY_ID(name)

    def set_avatar_if_not_set(self):
        a = self.driver.find_elements_by_id('')
        if len(a) == 0:
            pass
        else:
            self.driver.press_keycode(4)

    def is_exist_by_element_id(self, element_id: str) -> bool:
        self.wait_by_id(element_id, 10)
        assert len(self.driver.find_elements_by_id(element_id)) > 0

    def is_exist_by_element_class(self, element_class: str) -> bool:
        self.wait_by_class_name(element_class, 15)
        return len(self.driver.find_elements_by_class_name(element_class)) > 0

    def is_exist_obj(self, element):
        assert len(self.driver.find_elements(element)) > 0

    def put_text_to_input(self, text, element_id: str):
        input_text: WebElement = self.driver.find_element_by_id(element_id)
        input_text.clear()
        input_text.send_keys(text)

    def put_text_no_clear_to_input(self, text, element_id: str):
        input_text: WebElement = self.driver.find_element_by_id(element_id)
        input_text.send_keys(text)

    def put_text_to_element_input(self, text, element):
        input_text: WebElement = element
        input_text.clear()
        input_text.send_keys(text)

    def put_text_no_clear_to_element_input(self, text, element):
        input_text: WebElement = element
        input_text.send_keys(text)

    def open_avatar_in_edit_profile_options(self):
        self.wait_by_id('', 5)
        self.wait_by_id('', 5)
        self.wait_by_id('', 5)
        self.click_element_by_id('')
        self.wait_by_id('', 5)

    def sign_in(self, driver: webdriver, login: str, password: str) -> None:
        self.driver = driver
        sleep(2)
        assert self.click_element_by_id('')
        text_field = self.driver.find_elements_by_id('')
        self.put_text_to_input_obj(login, text_field[0])
        self.put_text_to_input_obj(password, text_field[1])
        assert self.click_element_by_id('')
        self.wait_by_id('', 5)

    def log_in(self, login: str, password: str) -> None:
        assert self.click_element_by_id('')
        text_field = self.driver.find_elements_by_id('')
        self.put_text_to_input_obj(login, text_field[0])
        self.put_text_to_input_obj(password, text_field[1])
        assert self.click_element_by_id('')


    def sign_out(self, driver: webdriver) -> None:
        pass

    def take_camera_photo_crop(self):
        allure.step('')
        self.click_element_by_id('')
        allure.step('')
        self.click_element_by_id('')
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        allure.step('')
        self.click_element_by_id('')
        sleep(3)

    def take_camera_photo_without_crop(self):
        allure.step('')
        self.click_element_by_id('')
        allure.step('')
        self.click_element_by_id('')
        allure.step('')
        self.click_element_by_id('')
        sleep(3)

    def make_screenshot(self):
        self.click_element_by_id('')
        sleep(5)
        self.click_element_by_id('')
        self.click_element_by_id('')

    def push_until_photo_saved(self):
        while len(self.driver.find_elements_by_id('')) == 0:
            self.click_element_by_id('')
        else:
            pass

    def random_choice_from_library(self):
        self.wait_by_id('', 15)
        allure.step('')
        self.click_element_by_id('')
        allure.step('')
        self.wait_by_id('', 15)
        photo_parent_block = self.driver.find_element_by_id('')
        all_photo = photo_parent_block.find_elements_by_id('')
        photo = random.choice(tuple(all_photo))
        photo.click()
        allure.step('')
        self.click_element_by_id('')
        sleep(1)

    def random_choice_crop_use_from_library(self):
        allure.step('')
        self.click_element_by_id('')
        allure.step('')
        self.wait_by_id('', 15)
        self.wait_by_id('', 15)
        photo_parent_block = self.driver.find_element_by_id('')
        all_photo = photo_parent_block.find_elements_by_id('')
        photo = random.choice(tuple(all_photo))
        photo.click()
        allure.step('')
        assert self.click_element_by_id('')
        self.click_element_by_id('')
        sleep(2)

    def profile_popup_exist_close(self):
        self.is_exist_by_element_id('')
        bubble_text = self.driver.find_element_by_id('').text
        assert bubble_text == '.'
        self.click_element_by_id('')
        self.is_exist_by_element_id('')
        assert EC.NoSuchElementException

    def not_exist_by_id(self, element_id: str) -> bool:
        self.wait_by_id(element_id, 5)
        return len(self.driver.find_elements_by_id(element_id)) == 0

    def not_exist_by_class(self, element_class: str) -> bool:
        self.wait_by_id(element_class, 2)
        return len(self.driver.find_elements_by_id(element_class)) == 0

    def not_exist_obj(self, obj):
        assert obj
        return len(obj) == 0

    def swipe_left_screen(self):
        size = self.driver.get_window_size()
        # Screen width width
        x = size['width']
        # The height of the screen height
        y = size['height']
        x1 = x * 0.9
        y1 = y * 0.5
        x2 = y * 0.1
        t = 1000
        n = 1  # n indicates the number of swipes
        sleep(1)
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_right_screen(self):
        size = self.driver.get_window_size()
        # Screen width width
        x = size['width']
        # The height of the screen height
        y = size['height']
        x1 = x * 0.1
        y1 = y * 0.5
        x2 = y * 0.9
        t = 1000
        n = 1  # n indicates the number of swipes
        sleep(1)
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_down_screen(self):
        size = self.driver.get_window_size()
        # Screen width width
        x = size['width']
        # The height of the screen height
        y = size['height']
        x1 = x * 0.6
        y1 = y * 0.1
        y2 = y * 0.9
        t = 1000
        n = 1  # n indicates the number of swipes
        sleep(1)
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_up_screen(self):
        size = self.driver.get_window_size()
        # Screen width width
        x = size['width']
        # The height of the screen height
        y = size['height']
        x1 = x * 0.6
        y1 = y * 0.9
        y2 = y * 0.1
        t = 1000
        n = 1  # n indicates the number of swipes
        sleep(1)
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)


    def swipe_right(self):
        assert self.driver.swipe(start_x=800, start_y=1000, end_x=200, end_y=1000)

    def swipe_left(self):
        assert self.driver.swipe(start_x=200, start_y=1000, end_x=800, end_y=1000)

    def swipe_down(self):
        assert self.driver.swipe(start_x=890, start_y=890, end_x=890, end_y=2050)

    def swipe_up(self):
        assert self.driver.swipe(start_x=890, start_y=2050, end_x=890, end_y=890)

    def long_press_options_publish_click(self, object):
        self.long_press_obj(object)
        self.click_element_by_id('')
        sleep(1)

    def long_press_options_col_publish_click(self, object):
        self.long_press_obj(object)
        self.click_element_by_id('')
        sleep(1)

    def long_press_options_unpublish_click(self, object):
        self.long_press_obj(object)
        self.click_element_by_id('')
        sleep(1)

    def long_press_options_col_unpublish_click(self, object):
        self.long_press_obj(object)
        self.click_element_by_id('')
        sleep(1)

    def long_press_options_delete_click(self, object):
        self.long_press_obj(object)
        menu = self.driver.find_element_by_class_name('')
        publish = menu.find_element_by_xpath("//*[@text='']")
        publish.click()
        sleep(5)

    def long_press_options_save_click(self, object):
        self.long_press_obj(object)
        menu = self.driver.find_element_by_class_name('android.widget.ListView')
        publish = menu.find_element_by_xpath("//*[@text='']")
        publish.click()
        sleep(5)

    def while_save_public_to_profile(self):
        self.wait_by_id('', 15)
        self.driver.find_element_by_id('')
        self.driver.find_element_by_id('')
        public_but = self.driver.find_element_by_id('')
        text1 = public_but.find_element_by_id('').text == ''
        assert text1
        text2 = public_but.find_element_by_id(
            '').text == ''
        assert text2
        self.click_element_by_id('')
        sleep(5)

    def while_save_drafts(self):
        self.wait_by_id('', 15)
        self.driver.find_element_by_id('')
        self.driver.find_element_by_id('')
        drafts = self.driver.find_element_by_id('')
        text1 = drafts.find_element_by_id('').text == ''
        assert text1
        text2 = drafts.find_element_by_id(
            '').text == ''
        assert text2
        self.click_element_by_id('')
        sleep(5)

    def while_save_cancel(self):
        self.wait_by_id('', 15)
        self.driver.find_element_by_id('')
        self.driver.find_element_by_id('')
        text = self.driver.find_element_by_id('').text == ''
        assert text
        self.click_element_by_id('')
        sleep(5)

    def wait_by_class_name(self, element_class_name: str, timeout: int) -> None:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, element_class_name))
        self.__wait(element_present, timeout)

    def wait_by_id(self, element_id: str, timeout: int) -> None:
        element_present = EC.presence_of_element_located((By.ID, element_id))
        self.__wait(element_present, timeout)

    def wait_by_id(self, element_id: str, timeout: int) -> None:
        element_present = EC.presence_of_element_located((By.ID, element_id))
        self.__wait(element_present, timeout)

    def wait_element(self, element, timeout: int) -> None:
        element_present = EC.presence_of_element_located(element)
        self.__wait(element_present, timeout)

    def wait_by_class(self, element_class: str, timeout: int) -> None:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, element_class))
        self.__wait(element_present, timeout)

    def wait_by_classes(self, elements_class: str, timeout: int) -> None:
        elements_present = EC.presence_of_all_elements_located((By.CLASS_NAME, elements_class))
        self.__wait(elements_present, timeout)

    def __wait(self, element_present, timeout: int) -> None:
        """
        :param timeout: Number of seconds before timing out
        """
        try:
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print('Timed out waiting for page to load')

    def web_random_text_pre_config_without_photo(self, text):
        self.click_element_by_id('')
        self.wait_by_id('', 15)
        urls = [

        ]
        search_url = random.choice(urls)
        self.put_text_to_input(search_url, '')
        # self.driver.press_keycode(23)
        self.tap_enter_button_prop_screen(1)

        # self.tap_by_coordinates(1320, 2271, 1)
        self.click_element_by_id('')
        self.put_text_to_input(text, '')
        self.click_element_by_id('')
        discription_text = self.random_text(4000)
        self.put_text_to_input(discription_text, '')
        self.driver.hide_keyboard()
        self.driver.press_keycode(4)

    def random_profile(self):
        profiles_to_test = []
        return random.choice(profiles_to_test)