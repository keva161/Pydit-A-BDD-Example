import selenium.webdriver
import pytest

@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    yield b
    b.quit()