from tests.common.base import *
from tests.login.locators.login_locators import *
from tests.config.settings import facebook_url


class LoginPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        super(LoginPage, self).__init__(driver)

    # Login to Facebook web app
    def login(self, username=None, password=None):
        driver = self.driver
        self.open(facebook_url)
        self.clear_element(username_txt_loc, 'id')
        self.set_value(username_txt_loc, username, 'id')
        self.set_value(password_txt_loc, password, 'id')
        self.click(login_button_loc)
        return driver
