import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_assertion():
    assert 1 + 2 == 3


@pytest.fixture
def driver():
    opts = Options()
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()


def test_check_google(driver):
    url = 'https://www.google.com/'

    driver.get(url)

    assert driver.title == 'Google'
    assert driver.current_url == url


def test_check_github(driver):
    url = 'https://github.com/'

    driver.get(url)

    assert driver.title != 'GitHub'
    assert driver.current_url == url
