from tests.facebook_user_actions.conftest import *

@pytest.mark.usefixtures("driver","driver_local", "share_post_on_fb_data")
class TestUserActions:
    @classmethod
    def setup_class(cls):
        LoginPage(cls.driver).login(username_one, password_one)
        cls.home_page = FbUserActions(cls.driver)


    def test_add_post(self):
        actual_posted_data = self.home_page.share_post(self.data_to_post['plain_text_post'])
        assert actual_posted_data['data'] == self.data_to_post['plain_text_post']
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_add_post_with_emoji(self):
        actual_posted_data = self.home_page.share_post(self.data_to_post['plain_text_post'], with_attachment=False,
                                                       video=False, with_emoji=True)
        assert actual_posted_data['data'] == self.data_to_post['plain_text_post_with_emoji']
        assert actual_posted_data['emoji'] is True
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_add_empty_post(self):
        actual_posted_data = self.home_page.share_post('')
        assert actual_posted_data['button_status'] is False
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_post_with_image_and_text(self):
        actual_posted_data = self.home_page.share_post(self.data_to_post['plain_text_post'], True)
        assert actual_posted_data['data'] == self.data_to_post['plain_text_post']
        assert actual_posted_data['image'] is True
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_post_only_image(self):
        actual_posted_data = self.home_page.share_post(None, True)
        assert actual_posted_data['image'] is True
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_post_with_video_and_text(self):
        actual_posted_data = self.home_page.share_post(self.data_to_post['plain_text_post'], True, True)
        assert actual_posted_data['data'] == self.data_to_post['plain_text_post']
        assert actual_posted_data['video'] is True
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_post_with_only_video(self):
        actual_posted_data = self.home_page.share_post(None, True, True)
        assert actual_posted_data['video'] is True
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_edit_post(self):
        actual_posted_data = self.home_page.share_post(self.data_to_post['plain_text_post'])
        assert actual_posted_data['data'] == self.data_to_post['plain_text_post']
        edited_post_data = self.home_page.edit_post("This is the edited post")
        assert edited_post_data['data'] == "This is the edited post"
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True

    def test_delete_post(self):
        actual_posted_data = self.home_page.share_post(self.data_to_post['plain_text_post'])
        assert actual_posted_data['data'] == self.data_to_post['plain_text_post']
        is_deleted = self.home_page.delete_post()
        assert is_deleted is True





