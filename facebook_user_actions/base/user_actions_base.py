from tests.common.base import *
from tests.facebook_user_actions.locators.user_actions_locators import *

class UserActionsBase(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        super(UserActionsBase, self).__init__(driver)

    def read_shared_post(self,with_attachment=False, video=False,with_emoji = False):
        posted_data = {}
        smiley_to_select = ""
        posted_data['data'] = str(self.get_text("(//*[contains(@class,'userContent')]//p)[1]"))
        if with_attachment is True:
            posted_data['image'] = self.is_displayed(assert_image_loc)
            if with_emoji:
                if posted_data['data'].__contains__(smiley_to_select):
                    posted_data['emoji'] = True
            if video is True:
                posted_data['video'] = self.is_displayed(assert_video_loc)
        return posted_data

    def read_message(self,sent_message):
        posted_message = {}
        self.click(messenger_icon_loc)
        self.click(select_message_content_loc)
        posted_message["message"] = self.is_displayed(read_message_txt_loc.format(sent_message))
        return posted_message["message"]














