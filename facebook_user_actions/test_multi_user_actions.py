from tests.facebook_user_actions.conftest import *


@pytest.mark.usefixtures("driver", "share_post_on_fb_data")
class TestMultiUserActions:
    @classmethod
    def setup_class(cls):
        LoginPage(cls.driver).login(username_two, password_two)
        cls.home_page = FbUserActions(cls.driver)

    ''''Multi user scenario'''

    def test_user_two_read_shared_post(self):
        actual_posted_data = self.home_page.share_post(self.data_to_post['plain_text_post'])
        assert actual_posted_data['data'] == self.data_to_post['plain_text_post']
        LoginPage(self.driver_local).login(username_two, password_two)
        check_posted_data = self.home_page.read_shared_post(self.data_to_post['plain_text_post'])
        print("read posted data", check_posted_data['data'])
        assert check_posted_data['data'] == actual_posted_data['data']
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_user_two_comment_on_shared_post(self):
        actual_posted_data = self.home_page.share_post(self.data_to_post['plain_text_post'])
        assert actual_posted_data['data'] == self.data_to_post['plain_text_post']
        LoginPage(self.driver_local).login(username_two, password_two)
        check_posted_data = self.home_page.read_shared_post(self.data_to_post['plain_text_post'])
        print("read posted data", check_posted_data['data'])
        assert check_posted_data['data'] == actual_posted_data['data']
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_send_message(self):
        message_data = {}
        message_data["recipient"] = "Charlie"
        message_data["message"] = "Hi Charlie!!"
        self.home_page.send_message(message_data)
        LoginPage(self.driver_local).login(username_two, password_two)
        sent_message = UserActionsBase(self.driver_local).read_message("Hi Charlie")
        assert sent_message is True
        message_data["recipient"] = "Harry"
        message_data["message"] = "Hi Harry!!"
        FbUserActions(self.driver_local).send_message(message_data)
        sent_message = self.home_page.read_message(message_data["message"])
        assert sent_message is True