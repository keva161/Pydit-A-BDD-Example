# PyDit (A Selenium BDD example)

A simple bot written in Python 3.8 that uses Selenium to access Reddit, interact with the webpages and downloads a lovely picture.

This is written purely for fun but will act as a great example of how to use BDD to drive your automation test case development.

Here are the results that must be achieved:

1. The browser must load up http://reddit.com using Chrome.
2. The bot should find the search box and type in 'memes' and submit the query.
3. On the results page, the 'r/memes' sub-reddit link should be clicked on.
4. On the sub-reddit page, the first post should be clicked on.
5. The photo in post should be downloaded.
6. The browser should close and you will have a nice new meme :)

PyTest will also be used to ensure that all these steps are passing.

To run the test you will need Python, PIPenv, Selenium and Pytest.

Then run the command `pipenv run python -m pytest`.

![](https://kevintuck.co.uk/images/meme.png)
