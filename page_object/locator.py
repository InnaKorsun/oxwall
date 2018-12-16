from selenium.webdriver.common.by import By

SIGN_IN = (By.XPATH,"//*[contains(@class,'ow_signin_label')]")

#login page

LOGIN_USERNAME_FIELD = (By.XPATH,"//input[contains(@name, 'identity')]")
LOGIN_PASSWORD_FIELD = (By.XPATH,"//input[contains(@name,'password')]")
LOGIN_SUBMIT= (By.XPATH,"//input[contains(@name,'submit')]")
JOIN_BUTTON = ('.//div[@class="ow_sign_up"]/p[2]/a')

#newsfeed field(add and delete)
class StatusLocator:
    NEWS_FIELD = (By.XPATH, "//textarea[contains(@name,'status')]")
    SEND_BUTTON = (By.NAME, "save")
    NEWS_PRESENT_FIELDS = (By.CLASS_NAME,"ow_newsfeed_content")
    NEWS_BODY = (By.CLASS_NAME,"ow_newsfeed_body")
    NEWS_DELETE_ITEM = (By.XPATH,"//div[contains(@class,'ow_context_action')]")
    NEW_DELETE_BUTTON = (By.XPATH,"//a[contains(@class,'newsfeed_remove_btn owm_red_btn')]")
    ALERT_AGREE_DELETE = (By.TAG_NAME,"alert")
    TEXT_STATUS = (By.XPATH,"//*[contains(@class,'ow_newsfeed_content ow_smallmargin')]")

#comments to newsfeed
class CommentLocator:
    ADD_COMMENT_ICON = (By.XPATH,"//*[contains(@class,'newsfeed_comment_btn')]")
    COMMENT_BODY = (By.XPATH,"//textarea[@class='comments_fake_autoclick']")
    COMMENT_TEXT = (By.XPATH,"//div[@class ='ow_comments_content ow_smallmargin']")
    DELETE_COMMENT = (By.XPATH,"//div[@class='ow_comments_item_info']")
    DELETE_COMMENT_BUTTON = (By.XPATH,"//div[@class='ow_context_action']")
    DELETE_COMMENT_ITEM = (By.XPATH,"//ul[@class='ow_context_action_list ow_border']/li/a")

#sign_out
class SignOutLocator:
    MENU_USER = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")
    MENU_USER_SIGN_OUT_OPTION = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_cont')]")


class InternalPageLocators:
    ACTIVE_MENU = (By.XPATH, "//div[contains(@class, 'ow_menu_wrap')]//li[contains(@class, 'active')]")
    MAIN_MENU = ()
    DASHBOARD_MENU = (By.LINK_TEXT, "DASHBOARD")
    SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
    SIGN_OUT_MENU = (By.XPATH, './/a[contains(@href,"sign-out")]')
    USER_MENU = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")

class SignInLocators:
    LOGIN_FIELD = (By.NAME, 'identity')
    PASS_FIELD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.XPATH, "//div[@class='ow_right']")
    LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")