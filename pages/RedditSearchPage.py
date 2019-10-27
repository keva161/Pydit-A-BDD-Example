
"""
This file contains the methods and elements for interacting with the Reddit search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class RedditSearchPage:

    def __init__(self, browser):
        self.browser = browser

    def ClickOnSubreddit(self):
        subreddit = self.browser.find_element_by_xpath("//div[text()='r/memes']")
        subreddit.click()
        
