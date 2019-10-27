"""
This file contains the methods and elements for interacting with the Reddit home page.
"""
import selenium.webdriver

class RedditHomePage:

    def __init__(self, browser):
        self.browser = browser

    def GoTo(self):
        self.browser.get("http://reddit.com")
        
    def SearchForMemes(self):
        self.browser.find_element_by_id("header-search-bar")
