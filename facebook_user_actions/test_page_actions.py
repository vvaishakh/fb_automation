from tests.facebook_user_actions.conftest import *
from tests.config.settings import *


@pytest.mark.usefixtures("driver", "driver_local", "page_data")
class TestFbPageActions:
    @classmethod
    def setup_class(cls):
        LoginPage(cls.driver).login(username_one, password_one)
        cls.fb_user_page = FbUserPage(cls.driver)

    def test_create_page(self):
        actual_page_data = self.fb_user_page.create_page(page_data)
        assert actual_page_data["page_name"] == page_data["page_name"]
        is_page_deleted = self.fb_user_page.delete_fb_page(page_data)
        assert is_page_deleted is True

    def test_add_post(self):
        actual_page_data = self.fb_user_page.create_page(page_data)
        assert actual_page_data["page_name"] == page_data["page_name"]
        actual_posted_data = self.fb_user_page.post_on_page(page_data)
        assert actual_posted_data == page_data["page_post"]
        is_page_deleted = self.fb_user_page.delete_fb_page(page_data)
        assert is_page_deleted is True

    def test_comment_on_post(self):
        actual_page_data = self.fb_user_page.create_page(page_data)
        assert actual_page_data["page_name"] == page_data["page_name"]
        LoginPage(self.driver_local).login(username_two, password_two)
        page_data["comment"] = "This is a comment on page"
        is_comment_added = self.fb_user_page.comment_on_page_post(page_data)
        assert is_comment_added is True
        is_page_deleted = self.fb_user_page.delete_fb_page(page_data)
        assert is_page_deleted is True

    def test_delete_comment(self):
        pass

    def test_delete_post(self):
        pass

    def test_delete_page(self):
        actual_page_data = self.fb_user_page.create_page(page_data)
        assert actual_page_data["page_name"] == page_data["page_name"]
        is_page_deleted = self.fb_user_page.delete_fb_page(page_data)
        assert is_page_deleted is True
