from selenium.webdriver.support.wait import WebDriverWait
from page_object import locators
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Oxwall:
    def __init__(self, driver):
        # Open Oxwall site
        self.driver = driver
        self.driver.get('http://127.0.0.1/oxwall/')
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def close(self):
        self.driver.quit()

    def login(self, username, password):
        sign_in = self.driver.find_element(*locators.SIGN_IN)
        sign_in.click()

        login_b = self.driver.find_element(*locators.LOGIN_USERNAME_FIELD)
        login_b.clear()
        login_b.send_keys("%s" % username)
        password_field = self.driver.find_element(*locators.LOGIN_PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys("%s" % password)

        button_sign = self.driver.find_element(*locators.LOGIN_SUBMIT)
        button_sign.click()

    def login_as(self, user):
        """ Login to Oxwall site by user"""
        driver = self.driver
        driver.find_element(*locators.SIGN_IN).click()
        login = driver.find_element(*locators.LOGIN_USERNAME_FIELD)
        login.click()
        login.send_keys(user["username"])
        passw = driver.find_element(*locators.LOGIN_PASSWORD_FIELD)
        passw.click()
        passw.send_keys(user["password"])
        driver.find_element(*locators.LOGIN_SUBMIT).click()
        # Wait until grey background disappeared
        #wait = WebDriverWait(driver, 5)
        #wait.until(expected_conditions.invisibility_of_element_located(locators.LOGIN_BACKGROUND))

    def add_new_text_status(self,test_text):
        newsfeed = self.driver.find_element(*locators.NEWS_FIELD)
        newsfeed.click()
        newsfeed.clear()
        newsfeed.click()
        newsfeed.send_keys(test_text)
        send_button = self.driver.find_element(*locators.NEWS_SEND_BUTTON)
        self.wait.until(expected_conditions.element_to_be_clickable, locators.NEWS_SEND_BUTTON)
        send_button.click()
        return test_text

    def get_newsfeed_list(self):
        return self.driver.find_elements(By.CLASS_NAME,"ow_newsfeed_content")

    def delete_news(self):
        news_body = self.driver.find_element(*locators.NEWS_BODY)
        news_body.click()
        delete_item = self.driver.find_elements(*locators.NEWS_DELETE_ITEM)[0]
        delete_item.click()
        time.sleep(1)
        delete_button = self.driver.find_elements(*locators.NEW_DELETE_BUTTON)[0]
        delete_button.click()

        time.sleep(3)
        self.driver.switch_to_alert().accept()

    def add_comment_to_newsfeed(self,text):

        add_comment_btns = self.driver.find_elements(*locators.NEWS_ADD_COMMENT_BTNS)
        add_comment_btns[0].click()

        comment_body = self.driver.find_elements(*locators.COMMENT_BODY)
        time.sleep(3)

        comment_body[0].send_keys(text)
        comment_body[0].send_keys(Keys.ENTER)

    def delete_comment_to_newsfeed(self):

        delete_comment_btns = self.driver.find_elements(*locators.DELETE_COMMENT_BUTTON)
        delete_comment_btns[0].click()

        delete_item = self.driver.find_elements(*locators.DELETE_COMMENT_ITEM)
        delete_item[1].click()
        self.driver.switch_to_alert().accept()


    def wait_until_new_status_appeared(self):
        # Wait until new status appear
        time.sleep(2)

    def logout(self):
        sign_out_all = self.driver.find_elements(*locators.MENU_USER)
        sign_out = sign_out_all[0]
        self.action.move_to_element(sign_out).perform()
        sign_out_option =self.driver.find_elements(*locators.MENU_USER_SIGN_OUT_OPTION)[5]
        self.action.pause(2)
        self.action.click(sign_out_option)
        self.action.perform()

    def logout_as(self, user):
        menu = self.driver.find_element(By.LINK_TEXT, user["username"].title())
        self.actions.move_to_element(menu).perform()
        self.driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()
