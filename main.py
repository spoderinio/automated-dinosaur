from selenium import webdriver
from selenium.webdriver.common.keys import Keys

GECKO_PATH = "E:\Development\geckodriver.exe"

driver = webdriver.Firefox(executable_path=GECKO_PATH)

driver.get("https://elgoog.im/t-rex/")


body = driver.find_element_by_xpath("/html/body")

body.send_keys(Keys.ARROW_UP)

bot_box = driver.find_element_by_xpath('//*[@id="botStatus"]')
bot_box.click()
