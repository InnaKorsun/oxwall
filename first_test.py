from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('http://127.0.0.1/oxwall/')
sign_in = driver.find_element_by_xpath("//*[contains(@class,'ow_signin_label')]")
#print(sign_in.text)
sign_in.click()

login = driver.find_element_by_xpath("//input[contains(@name, 'identity')]")
login.clear()
login.send_keys("admin")
password = driver.find_element_by_xpath("//input[contains(@name,'password')]")
password.clear()
password.send_keys("pass")

button_sign = driver.find_element_by_xpath("//input[contains(@name,'submit')]")
button_sign.click()

sign_out = driver.find_elements_by_xpath("//div[contains(@class,'ow_console_dropdown_hover')]")[0]

action = webdriver.ActionChains(driver)
action.move_to_element(sign_out).perform()
sign_out_option = driver.find_elements_by_xpath("//div[contains(@class,'ow_console_dropdown_cont')]")[5]

action.pause(2)
action.click(sign_out_option)
action.perform()

driver.quit()