from page_object import locator
from oxwall_site import Oxwall
from value_models.status import Status
from page_object.status_block import StatusBlock
import time


text = "Hello"

#add news
#def est_add_text_status(site, sign_in_session):
#    test_text = "Hello from selenium"
#    expected_text = test_text

#    site.add_new_text_status(test_text)
#    site.wait_until_new_status_appeared()
    # Verification that new status with this text appeared##
#     text_elements = site.get_newsfeed_list()
#   assert text_elements[0].text == expected_text



def test_add_text_status(driver, sign_in_session, admin_user):

    #app = Oxwall(driver)

    status = Status(text,user = admin_user)
    status_block  = StatusBlock(driver)

    status_block.add_new_status(status.text)
    status_block.wait_until_new_status_appeared()
    # Verification that new status with this text appeared
    time.sleep(3)
    text_elements = status_block.get_status_list()

    #user_status_elements = app.get_status_users()
    #time_status_elements = app.get_status_users()
    #
    print(text_elements[0].text)
    assert text_elements[0].text == text
    #assert status_block.user_element.text == status.user.real_name
    #assert status_block.time_element.text == "within 1 minute"













