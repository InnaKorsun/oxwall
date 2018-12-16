from page_object.page import Page
from page_object.locator import StatusLocator
import time
from selenium.webdriver.common.by import By
from page_object.locator import CommentLocator
from selenium.webdriver.common.keys import Keys


class StatusBlock(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.username_field = self.find_visible_element(locator.LOGIN_FIELD)

    @property
    def status_body(self):
        return self.find_visible_element(StatusLocator.NEWS_FIELD)

    @property
    def send_button(self):
        return self.find_visible_element(StatusLocator.SEND_BUTTON)

    @property
    def delete_button(self):
        return self.driver.find_elements(*StatusLocator.NEW_DELETE_BUTTON)

    @property
    def delete_item(self):
        return self.driver.find_elements(*StatusLocator.NEWS_DELETE_ITEM)

    def add_new_status(self, text_to_send):
        self.status_body.send_keys(text_to_send)
        self.send_button.click()

    def get_status_list(self):
        return self.driver.find_elements(*StatusLocator.TEXT_STATUS)
        #return self.driver.find_elements(By.CLASS_NAME,"ow_newsfeed_content")

    def delete_last_status(self):
        self.select_last_status()
        self.choose_delete_option()
        time.sleep(1)
        self.driver.switch_to_alert().accept()

    def select_last_status(self):
        #last_status = self.get_status_list()[0]
        last_status = self.driver.find_elements(*StatusLocator.NEWS_BODY)
        last_status[0].click()

    def choose_delete_option(self):

        delete_item = self.delete_item[0]
        delete_item.click()

        delete_button = self.delete_button[0]
        delete_button.click()

    def add_comment(self, text):
        self.select_last_status()
        icon = self.driver.find_elements(*CommentLocator.ADD_COMMENT_ICON)
        icon[0].click()

        comment_body = self.driver.find_elements(*CommentLocator.COMMENT_BODY)
        comment_body[0].clear()
        comment_body[0].send_keys(text)
        comment_body[0].send_keys(Keys.ENTER)

        comment_text = self.driver.find_element(*CommentLocator.COMMENT_TEXT)
        print(comment_text.text)
        return comment_text.text






