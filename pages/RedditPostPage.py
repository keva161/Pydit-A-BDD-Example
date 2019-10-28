
"""
This file contains the methods and elements for interacting with a Reddit post.
"""
from selenium.webdriver.common.by import By
import selenium
import urllib.request

class RedditPostPage:

    def __init__(self, browser):
        self.browser = browser

    def DownloadThePicture(self):
        img = []
        img = self.browser.find_elements_by_xpath("//img[contains(@alt, 'Post')]")
        
        urllib.request.urlretrieve(img[0].get_attribute("src"), "meme.png")

        
 