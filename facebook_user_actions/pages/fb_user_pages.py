from tests.facebook_user_actions.base.user_actions_base import *
from tests.facebook_user_actions.locators.user_actions_locators import *


class FbUserPage(UserActionsBase):
    def __init__(self, driver):
        self.driver = driver
        super(UserActionsBase, self).__init__(driver)


    def create_page(self, page_data):
        created_page = {}
        self.click(pages_link_loc)
        self.click(create_page_link_loc)
        self.click(community_page_button_loc)
        self.set_value(page_name_loc, page_data["page_name"])
        self.set_value(category_name_loc, page_data["page_desc"])
        self.click(continue_page_creation_button_loc)
        image_path = self.absolute_path(BASE_DIR + '/common/resources/fb_icon.png')
        self.upload_image(upload_image_loc, image_path)
        image_path = self.absolute_path(BASE_DIR + '/common/resources/hiking-fb-cover.jpg')
        self.upload_image(upload_cover_photo_loc, image_path)
        created_page["page_name"] = self.get_text(read_page_name_txt_loc)
        created_page["page_url"] = self.driver.current_url
        return created_page

    def post_on_page(self,page_data):
        self.open(page_data["page_url"])
        self.set_value(write_post_txt_loc, page_data["page_post"])
        self.click(publish_post_loc)
        page_post = self.get_text(read_page_post_txt_loc)
        return page_post

    def comment_on_page_post(self, page_data):
        is_comment_added = False
        self.open(page_data["page_url"])
        self.click(comment_button_loc)
        self.enter(comment_input_loc, page_data["comment"])
        read_comment = self.get_text(get_comment_loc)
        if read_comment == page_data["comment"]:
            is_comment_added = True
        return is_comment_added


    def delete_comment(self):
        pass


    def delete_page_post(self):
        pass

    def delete_fb_page(self,page_data):
        is_page_deleted = False
        self.open(page_data["page_url"])
        self.click(page_settings_link_loc)
        self.click(remove_page_link_loc)
        self.click(permanently_delete_page_link_loc.format(page_data["page_name"]))
        self.click(confirm_delete_page_loc)
        if self.is_displayed(page_deleted_popup_msg_loc):
            is_page_deleted = True
        return is_page_deleted
