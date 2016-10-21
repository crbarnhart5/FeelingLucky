from selenium import webdriver
import time, sys
search = input('Please enter your search')
browser = webdriver.Firefox()
browser.get('https://www.google.com/')
searchBar = browser.find_by_id('lst-ib')
searchBar.send_keys(Keys.chord(search))
browser.send_keys(Keys.ENTER)
