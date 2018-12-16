from page_object import locator
from oxwall_site import Oxwall
from value_models.status import Status
from page_object.status_block import StatusBlock
import time
text = "test Inna"

def test_delete_status(driver, sign_in_session, admin_user):


    status = Status(text, user=admin_user)
    status_block = StatusBlock(driver)

    status_block.add_new_status(status.text)
    status_block.wait_until_new_status_appeared()

    # Verification that new status with this text appeared
    a = status_block.get_status_list()
    assert a[0].text == text

    status_block.delete_last_status()
    status_block.refresh_page()
    status_block.wait_until_new_status_appeared()

    text_element = status_block.get_status_list()
    assert  text_element[0].text != text