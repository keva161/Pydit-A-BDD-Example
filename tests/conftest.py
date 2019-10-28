import selenium.webdriver
import pytest

@pytest.fixture
def browser():

    # The folloeing options block will start up Chrome without notifications enabled that could interfere with our test.

    chrome_options = selenium.webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    
    b = selenium.webdriver.Chrome(options=chrome_options)

    # Implicit waits are not advised. But including one here for demo purposes
    
    b.implicitly_wait(10)
    yield b
    b.quit()