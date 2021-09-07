#!/usr/bin/env python3

from selenium import webdriver
browser = webdriver.Firefox()  # it will open firefox
browser.get("http://google.com") # it wil go to google.com in firefox 

elem = browser.find_element_by_css_selector("#YOUR CSS SELE") # we can use xpath, or other option for selecting
elem.click() ## it will click that link or anything you choose

elems = browser.find_elements_by_css_selector("p") # -- it will contians all css p in the browser

searchElem = browser.find_element_by_css_selector("# your css selctor text of search box")
searchElem.send_keys("Harshit Raj Singh") # it will type harshit raj singh in the google search box
searchElem.submit() # it will submit the req and search for it

browser.back() # to go back we can also forwar(), refresh(), quit()

# to read the content

elem = browser.find_element_by_css_selector("#YOUR CSS SELE") # we can use xpath, or other option for selecting
elem.text ## it will select all the text inside that css selct you selct

# for entire webpage


elem = browser.find_element_by_css_selector("html") # we can use xpath, or other option for selecting
elem.text # contain entire webpase


