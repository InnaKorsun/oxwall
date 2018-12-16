from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from page_object import locator
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

    def login_as(self, user):
        """ Login to Oxwall site by user"""
        driver = self.driver
        driver.find_element(*locator.SIGN_IN).click()
        login = driver.find_element(*locator.LOGIN_USERNAME_FIELD)
        login.click()
        login.send_keys(user.username)
        passw = driver.find_element(*locator.LOGIN_PASSWORD_FIELD)
        passw.click()
        passw.send_keys(user.password)
        driver.find_element(*locator.LOGIN_SUBMIT).click()
        # Wait until grey background disappeared
        #wait = WebDriverWait(driver, 5)
        #wait.until(expected_conditions.invisibility_of_element_located(locators.LOGIN_BACKGROUND))

    # def add_new_text_status(self,status):
    #     newsfeed = self.driver.find_element(*locator.StatusLocator.NEWS_FIELD)
    #     newsfeed.click()
    #     newsfeed.clear()
    #     newsfeed.click()
    #     newsfeed.send_keys(status.text)
    #     send_button = self.driver.find_element(*locator.StatusLocator.NEWS_SEND_BUTTON)
    #     self.wait.until(expected_conditions.element_to_be_clickable, locator.StatusLocator.NEWS_SEND_BUTTON)
    #     send_button.click()
    #     #return test_text

    def get_newsfeed_list(self):
        return self.driver.find_elements(By.CLASS_NAME,"ow_newsfeed_content")

    # def delete_news(self):
    #     news_body = self.driver.find_element(*locator.NEWS_BODY)
    #     news_body.click()
    #     delete_item = self.driver.find_elements(*locator.NEWS_DELETE_ITEM)[0]
    #     delete_item.click()
    #     time.sleep(1)
    #     delete_button = self.driver.find_elements(*locator.NEW_DELETE_BUTTON)[0]
    #     delete_button.click()
    #
    #     time.sleep(3)
    #     self.driver.switch_to_alert().accept()

    def add_comment_to_newsfeed(self,text):

        add_comment_btns = self.driver.find_elements(*locator.NEWS_ADD_COMMENT_BTNS)
        add_comment_btns[0].click()

        comment_body = self.driver.find_elements(*locator.COMMENT_BODY)


        comment_body[0].send_keys(text)
        comment_body[0].send_keys(Keys.ENTER)

    def delete_comment_to_newsfeed(self):

        delete_comment= self.driver.find_elements(*locator.DELETE_COMMENT)
        self.actions.move_to_element(delete_comment[0]).perform()

        #delete_comment_btns[0].click()
        delete_button = self.driver.find_elements(*locator.DELETE_COMMENT_BUTTON).click()

        delete_item = self.driver.find_elements(*locator.DELETE_COMMENT_ITEM)
        delete_item[1].click()
        self.driver.switch_to_alert().accept()

    def is_dashbord_page(self):
        return self.is_element_present(By.XPATH, "//h1[contains(., ‘My Dashboard’)]")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def wait_until_new_status_appeared(self):
        # Wait until new status appear
        time.sleep(2)


    def logout_as(self):
        menu = self.driver.find_element(*locator.SignOutLocator.MENU_USER)
        self.actions.move_to_element(menu).perform()
        self.driver.find_element(*locator.SignOutLocator.MENU_USER_SIGN_OUT_OPTION).click()


    def close(self):
        self.driver.quit()