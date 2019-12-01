from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By # to find an element
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.linkedin.com")
inputElement = driver.find_element_by_name("session_key")
inputElement.send_keys("user name")
inputElement.submit()

#no user name
if ("Please enter a valid email address" in driver.page_source):
     print("No email entered")

#bad user name
if ("Please enter a valid username" in driver.page_source):
     print("Invalid user name entered")

inputElement = driver.find_element_by_name("session_password")
inputElement.send_keys("password")
inputElement.submit()

#no password
if ("Please enter a password" in driver.page_source):
     print("No password entered")

#bad password
if ("Please enter a valid username" in driver.page_source):
     print("wrong password entered")

driver.quit()


