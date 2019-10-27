
"""
These tests will cover the required functionality for our Selenium bot.
"""

from pages.RedditHomePage import RedditHomePage
from pages.RedditSearchPage import RedditSearchPage
from pages.RedditSubRedditPage import RedditSubRedditPage
from pages.RedditPostPage import RedditPostPage

def test_pydit_functionality(browser):
    
    # Given that I want to goto Redditp
    HomePage = RedditHomePage(browser)
    HomePage.GoTo()

    # When I want to view the latest memes.
    HomePage.SearchForMemes()

    # Then I access the subreddit
    SearchPage = RedditSearchPage(browser)
    SearchPage.ClickOnSubreddit()
     
    # And I view the first post in the subreddit
    SubRedditPage = RedditSubRedditPage(browser)
    SubRedditPage.ClickOnFirstPost()
    
    # And I download the picture
    PostPage = RedditPostPage(browser)
    PostPage.DownloadThePicture()
    

    #raise Exception("Incomplete Test")