from page_object import locator
from oxwall_site import Oxwall
from value_models.status import Status
from page_object.status_block import StatusBlock

import time
text = "test Inna"
comme = "First comment"

def test_add_comment_to_status(driver, sign_in_session, admin_user):

    status = Status(text, user=admin_user)
    status_block = StatusBlock(driver)

    status_block.add_new_status(status.text)
    status_block.wait_until_new_status_appeared()

    status_block.select_last_status()
    comment_text = status_block.add_comment(comme)

    assert comme == comment_text










# #def est_delete_comment(site,sign_in_session,add_newsfeed):#
#
#     comment = "Ku-ku from"
#     site.add_comment_to_newsfeed(comment)
#     site.wait_until_new_status_appeared
#     site.delete_comment_to_newsfeed
