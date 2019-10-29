
"""
These tests will cover the required functionality for our Selenium bot.
"""

from pages.RedditHomePage import RedditHomePage
from pages.RedditSearchPage import RedditSearchPage
from pages.RedditSubRedditPage import RedditSubRedditPage
from pages.RedditPostPage import RedditPostPage

def test_pydit_functionality(browser):
    HomePage = RedditHomePage(browser)
    SearchPage = RedditSearchPage(browser)
    SubRedditPage = RedditSubRedditPage(browser)
    PostPage = RedditPostPage(browser)

    TITLE = "/r/Memes"
    
    
    # Given that I want to goto Reddit.
    HomePage.GoTo()

    # When I want to view the latest memes.
    HomePage.SearchForMemes()

    # Then I access the subreddit.
    SearchPage.ClickOnSubreddit()
     
    # And I view the first post in the correct subreddit.
    SubRedditPage.ClickOnFirstPost()
    
    assert TITLE in SubRedditPage.PageTitle()
    
    # And I download the picture.
    PostPage.DownloadThePicture()

    # The file should be present for me to view
    assert PostPage.FileHasDownloaded() == True

