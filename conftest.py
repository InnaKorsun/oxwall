import pytest
from oxwall_site import Oxwall
from selenium import webdriver

@pytest.fixture()
def driver():
    # Open browser driver settings
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    # Close browser
    driver.quit()

@pytest.fixture
def site(driver):
    app = Oxwall(driver)
    return app

@pytest.fixture()
def sign_in_session(site, user):
    site.login_as(user)
    yield
    site.logout_as(user)

@pytest.fixture
def add_newsfeed(site):
    text = "Should be deleted"
    site.add_new_text_status(text)
    return text


@pytest.fixture()
def user():
    return {"username": "admin", "password": "pass"}






