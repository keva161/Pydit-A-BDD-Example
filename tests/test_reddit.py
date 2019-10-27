
"""
These tests will cover the required functionality for our Selenium bot.
"""

from pages.RedditHomePage import RedditHomePage

def test_pydit_functionality(browser):
    
    # Given that I want to goto Redditp
    HomePage = RedditHomePage(browser)
    HomePage.GoTo()

    # When I want to view the latest memes.
    # # TODO
     
    # Then I view the first post in the subreddit
    # TODO
    
    # And I download the picture
    # TODO
    
    # And I the browser closes
    # TODO

    raise Exception("Incomplete Test")