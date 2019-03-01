from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    web_driver = webdriver.Chrome(chrome_options=chrome_options)
    web_driver.fullscreen_window()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", web_driver)
    # LoginPage(web_driver).login('username','password')
    yield
    web_driver.close()

@pytest.fixture(scope="session")
def driver_local(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    web_driver = webdriver.Chrome(chrome_options=chrome_options)
    web_driver.fullscreen_window()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver_local", web_driver)
    # LoginPage(web_driver).login('username','password')
    yield
    web_driver.close()