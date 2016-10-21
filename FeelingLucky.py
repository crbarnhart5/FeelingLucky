from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
search = input('Please enter your search: ')
browser = webdriver.Firefox()
browser.get('https://www.google.com/')
time.sleep(5) #Waits for page to load
searchBar = browser.find_element_by_id('lst-ib')
searchBar.click()
searchBar.send_keys(search)
time.sleep(2)
searchBar.send_keys(Keys.ENTER)
