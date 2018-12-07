import pytest
from selenium.webdriver.common.by import By
from time import sleep
from page_object import locators


#add news
def est_add_text_status(site, sign_in_session):
    test_text = "Hello from selenium"
    expected_text = test_text

    site.add_new_text_status(test_text)
    site.wait_until_new_status_appeared()
    # Verification that new status with this text appeared
    text_elements = site.get_newsfeed_list()
    assert text_elements[0].text == expected_text

#@pytest.mark()
def est_delete_text_status(site,sign_in_session,add_newsfeed,delete_news):

    expected_text = add_newsfeed
    text_elem = site.driver.find_elements(*locators.NEWS_PRESENT_FIELDS)
    print(text_elem[1].text)
    assert text_elem[1].text != expected_text

def est_add_commnt_to_newsfeed(site,sign_in_session):
    site.add_new_text_status("Inna")
    site.wait_until_new_status_appeared
    comment = "Ku"
    site.add_comment_to_newsfeed(comment)
    #comment_body = site.driver.find_elements(*locators.COMMENT_BODY)

def test_delete_comment(site,sign_in_session):
    site.add_new_text_status("Inna")
    site.wait_until_new_status_appeared
    comment = "Ku-ku"
    site.add_comment_to_newsfeed(comment)
    #comment_body = site.driver.find_elements(*locators.COMMENT_BODY)
    site.wait_until_new_status_appeared
    site.delete_comment_to_newsfeed













