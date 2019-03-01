from tests.login.conftest import *
from tests.login.locators.login_locators import *


@pytest.mark.usefixtures("driver","invalid_login_data")
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.login_page = LoginPage(cls.driver)

    def assertions(self, error_loc):
        if self.login_page.is_displayed(error_loc):
            assert True

    def test_valid_login(self):
        self.login_page.login(username_one, password_one)
        if self.login_page.is_displayed(fb_post_txt_loc,'id'):
            assert True
            self.login_page.click(navigation_icon_loc,'id')
            self.login_page.click(logout_loc)

    def test_invalid_email(self):
        self.login_page.login(self.invalid_login_data['username'], password_one)
        self.assertions(login_email_error_popover_loc)

    def test_invalid_password(self):
        self.login_page.login(username_one, self.invalid_login_data['password'])
        self.assertions(login_password_error_popover_loc)

    def test_login_with_empty_creds(self):
        self.login_page.login('', '')
        self.assertions(login_email_error_popover_loc)

    def test_login_with_only_email(self):
        self.login_page.login(username_one, '')
        self.assertions(login_password_error_popover_loc)

    def test_login_with_only_password(self):
        self.login_page.login('', password_one)
        self.assertions(login_email_error_popover_loc)

    def test_login_with_invalid_creds(self):
        self.login_page.login(self.invalid_login_data['username'], self.invalid_login_data['password'])
        self.assertions(login_email_error_popover_loc)
