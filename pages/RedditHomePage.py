"""
This file contains the methods and elements for interacting with the Reddit home page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class RedditHomePage:

    def __init__(self, browser):
        self.browser = browser

    def GoTo(self):
        self.browser.get("http://reddit.com")
        
    def SearchForMemes(self):
        search_box = self.browser.find_element_by_name("q")
        search_box.send_keys("memes" + Keys.RETURN)
