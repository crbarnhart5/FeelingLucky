from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys

search = input('Please enter your search: ')
browser = webdriver.Firefox()
browser.get('https://www.google.com/')
time.sleep(3) #Waits for page to load

searchBar = browser.find_element_by_id('lst-ib')
searchBar.click()
searchBar.send_keys(search)
time.sleep(1)
searchBar.send_keys(Keys.ENTER)

time.sleep(3) #Wait for page to load
firstLink = browser.find_element_by_xpath('//*[@id="rso"]/div/div/h3/a')
firstLink.click()

sys.exit()
