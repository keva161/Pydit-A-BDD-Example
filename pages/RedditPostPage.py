
"""
This file contains the methods and elements for interacting with a Reddit post.
"""
from selenium.webdriver.common.by import By
import selenium.webdriver
import urllib.request

import urllib

class RedditPostPage:

    def __init__(self, browser):
        self.browser = browser

    def DownloadThePicture(self):
        with open('meme.png', 'wb') as file:
            file.write(self.browser.find_elements_by_xpath("//a[img]")[1].screenshot_as_png)