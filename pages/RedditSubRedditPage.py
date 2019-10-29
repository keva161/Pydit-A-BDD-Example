
"""
This file contains the methods and elements for interacting with the Reddit memes subreddit.
"""
import selenium.webdriver.common.by
import selenium.webdriver.common.keys

class RedditSubRedditPage:

    def __init__(self, browser):
        self.browser = browser

    def ClickOnFirstPost(self):
        post = self.browser.find_elements_by_xpath("//h3")[0]
        post.click()

    def PageTitle(self):
        return self.browser.title


