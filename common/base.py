import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import Keys
import os

wait_time = 2
xpath = 'xpath'
classes = 'class'
_id = 'id'
link_text = 'linkText'
tag = 'tag'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def open(self, value):
        self.driver.get(value)

    def click(self, value, loc_type=xpath, _wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, value))).click()
                    break
                elif loc_type == 'class':
                    wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, value))).click()
                    break
                elif loc_type == 'id':
                    wait.until(expected_conditions.element_to_be_clickable((By.ID, value))).click()
                    break
                elif loc_type == 'linkText':
                    wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, value))).click()
                    break
            except Exception as e:
                print(e)
                continue

    def set_value(self, value, text_input, loc_type=xpath, _wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, value))).send_keys(
                        text_input)
                    break
                elif loc_type == 'class':
                    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, value))).send_keys(
                        text_input)
                    break
                elif loc_type == 'id':
                    wait.until(expected_conditions.visibility_of_element_located((By.ID, value))).send_keys(text_input)
                    break
            except Exception as e:
                print(e)
                continue

    def clear_element(self, value, loc_type=xpath, _wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, value))).clear()
                    break
                elif loc_type == 'class':
                    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, value))).clear()
                    break
                elif loc_type == 'id':
                    wait.until(expected_conditions.visibility_of_element_located((By.ID, value))).clear()
                    break
            except Exception as e:
                print(e)
                continue

    # Function to Clear a field and Enter a new value into a field
    def clear_send_keys(self, value, text_input, _wait_time=5):
        self.clear_element(value, _wait_time=_wait_time)
        self.set_value(value, text_input, _wait_time=_wait_time)

    def get_text(self, value, loc_type=xpath, _wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    return wait.until(expected_conditions.visibility_of_element_located((By.XPATH, value))).text
                elif loc_type == 'class':
                    return wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, value))).text
                elif loc_type == 'id':
                    return wait.until(expected_conditions.visibility_of_element_located((By.ID, value))).text
                elif loc_type == 'linkText':
                    return wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, value))).text
            except Exception as e:
                print(e)
                continue
        return False

    def is_displayed(self, value, loc_type=xpath, _wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    return wait.until(
                        expected_conditions.visibility_of_element_located((By.XPATH, value))).is_displayed()
                elif loc_type == 'class':
                    return wait.until(
                        expected_conditions.visibility_of_element_located((By.CLASS_NAME, value)))
                elif loc_type == 'id':
                    return wait.until(expected_conditions.visibility_of_element_located((By.ID, value)))
                elif loc_type == 'linkText':
                    return wait.until(
                        expected_conditions.visibility_of_element_located((By.LINK_TEXT, value))).is_displayed()
            except Exception as e:
                print(e)
                continue
        return False

    def is_enabled(self, value, loc_type=xpath, _wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    return wait.until(
                        expected_conditions.visibility_of_element_located((By.XPATH, value))).is_enabled()
                elif loc_type == 'class':
                    return wait.until(
                        expected_conditions.visibility_of_element_located((By.CLASS_NAME, value)))
                elif loc_type == 'id':
                    return wait.until(expected_conditions.visibility_of_element_located((By.ID, value)))
                elif loc_type == 'linkText':
                    return wait.until(
                        expected_conditions.visibility_of_element_located((By.LINK_TEXT, value))).is_enabled()
            except Exception as e:
                print(e)
                continue
        return False

    def find_element(self, value, loc_type=xpath, _wait_time=0):
        wait = WebDriverWait(self.driver, _wait_time)
        try:
            if loc_type == 'xpath':
                return wait.until(expected_conditions.visibility_of_element_located((By.XPATH, value)))
            elif loc_type == 'class':
                return wait.until(
                    expected_conditions.visibility_of_element_located((By.CLASS_NAME, value)))
            elif loc_type == 'id':
                return wait.until(expected_conditions.visibility_of_element_located((By.ID, value)))
            elif loc_type == 'linkText':
                return wait.until(
                    expected_conditions.visibility_of_element_located((By.LINK_TEXT, value)))
            elif loc_type == "tag":
                return wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, value)))
        except Exception as e:
            print(e)
            return False

    def upload_image(self, value, image_path, loc_type=xpath):
        wait = WebDriverWait(self.driver, wait_time)
        if loc_type == 'xpath':
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, value))).send_keys(image_path)
        elif loc_type == 'class':
            wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, value))).send_keys(image_path)
        elif loc_type == 'id':
            wait.until(expected_conditions.presence_of_element_located((By.ID, value))).send_keys(image_path)

    def find_elements(self, value, loc_type=xpath):
        if loc_type == 'xpath':
            return self.driver.find_elements_by_xpath(value)
        elif loc_type == 'id':
            return self.driver.find_elements_by_id(value)
        elif loc_type == 'class':
            return self.driver.find_elements_by_class_name(value)
        elif loc_type == 'tag':
            return self.driver.find_elements_by_tag_name(value)

    def move_to_element(self, loc_type='xpath', value1=None, value2=None, value3=None, value4=None):
        actions = ActionChains(self.driver)
        if loc_type == 'xpath':
            if value2 and value3 is not None:
                actions.move_to_element(self.driver.find_element_by_xpath(value1)).move_to_element(
                    self.driver.find_element_by_xpath(value2)).move_to_element(
                    self.driver.find_element_by_xpath(value3)).move_to_element(
                    self.driver.find_element_by_xpath(value4)).click().perform()
            else:
                actions.move_to_element(self.driver.find_element_by_xpath(value1))
        elif loc_type == 'id':
            actions.move_to_element(self.driver.find_element_by_id(value1))
        elif loc_type == 'class':
            actions.move_to_element(self.driver.find_element_by_class_name(value1))

    def enter(self, value, text_input, loc_type=xpath, _wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    wait.until(expected_conditions.presence_of_element_located((By.XPATH, value))).send_keys(text_input)
                    self.find_element(value, loc_type).send_keys(Keys.ENTER)
                    break
                elif loc_type == 'class':
                    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, value))).send_keys(
                        text_input)
                    self.find_element(value, loc_type).send_keys(Keys.ENTER)
                elif loc_type == 'id':
                    wait.until(expected_conditions.presence_of_element_located((By.ID, value))).send_keys(text_input)
                    self.find_element(value, loc_type).send_keys(Keys.ENTER)
                elif loc_type == 'linkText':
                    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, value))).send_keys(
                        text_input)
                    self.find_element(value, loc_type).send_keys(Keys.ENTER)
            except Exception as e:
                print(e)
                continue

    def select_dropdown_value(self, dd_loc, dd_set_value_loc, dd_select_value_loc, text_input, loc_type=xpath,
                              _wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, dd_loc))).click()
                    wait.until(expected_conditions.visibility_of_element_located((By.XPATH,
                                                                                  dd_set_value_loc))).send_keys(
                        text_input)
                    self.click(dd_select_value_loc)
                    # wait.until(expected_conditions.element_to_be_clickable((By.XPATH, dd_select_value_loc))).click()
                    break
            except Exception as e:
                print(e)
                continue

    def select_from_dropdown_using_select(self, value, option, loc_type=xpath):
        if loc_type == 'xpath':
            return Select(self.driver.find_element_by_xpath(value)).select_by_index(option)
        elif loc_type == 'id':
            return Select(self.driver.find_element_by_id(value)).select_by_visible_text(option)
        elif loc_type == 'class':
            return Select(self.driver.find_element_by_class(value)).select_by_visible_text(option)

    def is_selected(self, locator, loc_type=xpath, _wait_time=5):
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    return self.driver.find_element_by_xpath(locator).is_selected()
                elif loc_type == 'id':
                    return self.driver.find_element_by_id(locator).is_selected()
                elif loc_type == 'class':
                    return self.driver.find_element_by_class(locator).is_selected()
            except Exception as e:
                print(e)
                continue

    def get_att(self, locator, attr_name, loc_type=xpath, _wait_time=5):
        for i in range(0, _wait_time):
            if i > 0:
                time.sleep(1)
            try:
                if loc_type == 'xpath':
                    return self.driver.find_element_by_xpath(locator).get_attribute(attr_name)
                elif loc_type == 'id':
                    return self.driver.find_element_by_id(locator).get_attribute(attr_name)
                elif loc_type == 'class':
                    return self.driver.find_element_by_class(locator).get_attribute(attr_name)
            except Exception as e:
                print(e)
                continue

    def absolute_path(self, path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), path))
