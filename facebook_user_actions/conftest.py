'''Config'''
from tests.config.settings import *

'''Fixtures'''
from tests.common.global_fixtures import *
from tests.facebook_user_actions.fixtures.fb_action_fixtures import *
from tests.facebook_user_actions.fixtures.fb_page_fixtures import *


'''Locators'''
from tests.facebook_user_actions.locators.user_actions_locators import *

"""Page"""
from tests.login.pages.login import LoginPage
from tests.facebook_user_actions.base.user_actions_base import UserActionsBase
from tests.facebook_user_actions.pages.user_home_page import FbUserActions
from tests.facebook_user_actions.pages.fb_user_pages import FbUserPage
