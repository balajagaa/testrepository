from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "vonceil@uetimer.com"
password = "upperandlowercaseletters"
driver = webdriver.Chrome()
driver.get('https://bugcrowd:wow wobbly whiplash barbecue@redama.com/user/sign_in')
element = driver.find_element_by_id("user_email")
element.send_keys(user_name)
element = driver.find_element_by_id("user_password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
driver.close()
driver.quit()