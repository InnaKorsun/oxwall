from selenium.webdriver.common.by import By

SIGN_IN = (By.XPATH,"//*[contains(@class,'ow_signin_label')]")

#login page

LOGIN_USERNAME_FIELD = (By.XPATH,"//input[contains(@name, 'identity')]")
LOGIN_PASSWORD_FIELD = (By.XPATH,"//input[contains(@name,'password')]")
LOGIN_SUBMIT= (By.XPATH,"//input[contains(@name,'submit')]")
JOIN_BUTTON = ('.//div[@class="ow_sign_up"]/p[2]/a')

#newsfeed field(add and delete)
NEWS_FIELD = (By.NAME, "status")
NEWS_SEND_BUTTON = (By.NAME, "save")
NEWS_PRESENT_FIELDS = (By.CLASS_NAME,"ow_newsfeed_content")
NEWS_BODY = (By.CLASS_NAME,"ow_newsfeed_body")
NEWS_DELETE_ITEM = (By.XPATH,"//span[contains(@class,'ow_context_more')]")
NEW_DELETE_BUTTON = (By.XPATH,"//a[contains(@class,'newsfeed_remove_btn owm_red_btn')]")
ALERT_AGREE_DELETE = (By.TAG_NAME,"alert")

#comments to newsfeed
NEWS_ADD_COMMENT_BTNS = (By.XPATH,"//*[contains(@class,'newsfeed_comment_btn')]")
COMMENT_BODY = (By.XPATH,"//textarea[@class='comments_fake_autoclick']")
DELETE_COMMENT_BUTTON = (By.XPATH,"//span[@class='ow_context_more']")
DELETE_COMMENT_ITEM = (By.XPATH,"//ul[@class='ow_context_action_list ow_border']/li/a")

#sign_out
MENU_USER = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")
MENU_USER_SIGN_OUT_OPTION = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_cont')]")


