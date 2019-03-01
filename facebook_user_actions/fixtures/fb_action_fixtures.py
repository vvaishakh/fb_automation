import pytest


@pytest.fixture(scope="session")
def share_post_on_fb_data(request):
    data_to_post = {
        "plain_text_post": "This is a plain text post",
        "post_with_link": "post data with link - https://www.accuweather.com/en/in/chennai/206671/current-weather/206671",
        "plain_text_post_with_emoji": "This is a plain text post😀"
    }
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "data_to_post", data_to_post)


# @pytest.fixture(scope="session")
# def share_post_on_fb_data():
#     data_to_post = {
#         "plain_text_post": "This is a plain text",
#         "post_with_link": "post data with link - https://www.accuweather.com/en/in/chennai/206671/current-weather/206671"
#     }
#     return data_to_post
