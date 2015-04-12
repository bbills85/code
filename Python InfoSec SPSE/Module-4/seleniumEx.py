#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

# need to install pip
# http://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/
# http://stackoverflow.com/questions/6682009/selenium-firefoxprofile-exception-cant-load-the-profile
