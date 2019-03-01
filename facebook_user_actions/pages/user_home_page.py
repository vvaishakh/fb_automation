from tests.facebook_user_actions.base.user_actions_base import *
from tests.facebook_user_actions.locators.user_actions_locators import *
import time

class FbUserActions(UserActionsBase):

    def share_post(self,post_data=None, with_attachment=False, video=False,with_emoji = False):
        posted_data = {}
        smiley_to_select = ""
        self.click(click_write_post_txt_loc)
        self.set_value(write_post_txt_loc, post_data)
        if with_emoji:
            self.click(add_emoji_icon_loc)
            smiley_to_select = self.get_att(smiley_img_loc,"alt")
            self.click(smiley_img_loc)
        if with_attachment:
            if video is True:
                video_path = self.absolute_path(BASE_DIR + '/common/resources/video.3gp')
                self.upload_image(upload_image_loc, video_path)
            else:
                image_path = self.absolute_path(BASE_DIR + '/common/resources/fb_icon.png')
                self.upload_image(upload_image_loc, image_path)

        if post_data is not None or with_attachment is True:
            self.click(share_post_btn_loc)
            import time
            time.sleep(3)
            posted_data['data'] = str(self.get_text("(//*[contains(@class,'userContent')]//p)[1]"))
            posted_data['image'] = self.is_displayed(assert_image_loc)
            print("from home",posted_data['data'])
            if with_emoji:
                if posted_data['data'].__contains__(smiley_to_select):
                    posted_data['emoji'] = True
            if video is True:
                posted_data['video'] = self.is_displayed(assert_video_loc)

        else:
            posted_data['button_status'] = self.is_enabled(share_post_btn_loc)
        return posted_data


    def edit_post(self, post_data=None, with_attachment=False, video=False):
        posted_data = {}
        self.click(post_options_loc.format('1'))
        self.click(edit_post_link_loc)
        self.set_value(write_post_txt_loc, post_data)
        if with_attachment is True and video is False:
            image_path = self.absolute_path(BASE_DIR + '/common/resources/fb_icon.png')
            self.upload_image(upload_image_loc, image_path)
        self.click(save_edited_post_btn_loc)
        if with_attachment:
            if video is True:
                posted_data['data'] = self.get_text("(//*[contains(@class,'userContent')]//p)[1]")
        posted_data['data'] = self.get_text("(//*[contains(@class,'userContent')]//p)[1]")
        return posted_data


    def delete_post(self):
        is_deleted = False
        for post in range(1, len(self.find_elements(all_post_options_loc))+1):
            self.click(post_options_loc.format(post))
            time.sleep(5)
            self.click(delete_post_link_loc)
            if self.is_displayed(delete_post_confirm_btn_loc,xpath):
                self.click(delete_post_confirm_btn_loc)
        self.click(profile_name_icon_loc)
        self.click(manage_posts_btn_loc)
        self.click(posted_by_you_lbl_loc)
        manage_posts_empty_state = self.get_text(no_posts_empty_state_loc)
        self.click(manage_posts_grid_view_btn_loc)
        manage_posts_grid_empty_state = self.get_text(no_posts_empty_state_loc)
        if manage_posts_empty_state.__contains__("No posts") and manage_posts_grid_empty_state.__contains__("No posts") :
            is_deleted = True
        return is_deleted

    def send_message(self,message_data):
        self.click(messenger_icon_loc)
        self.click(new_message_link_loc)
        self.select_dropdown_value(to_list_txt_loc, to_list_input_loc, select_recepient_option_loc, message_data["recipient"])
        self.click(message_area_txt_loc)
        self.enter(message_area_txt_loc,message_data["message"])








