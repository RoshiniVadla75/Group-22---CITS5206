from selenium.webdriver.common.by import By

BASE_URL = "http://127.0.0.1:5000"

def test_home_page_loads(browser):
    browser.get(BASE_URL)
    assert "Museum" in browser.page_source or "AI" in browser.page_source


def test_home_navbar_links(browser):
    browser.get(BASE_URL)
    page = browser.page_source

    assert "Home" in page
    assert "Timeline" in page
    assert "Guided Tour" in page


def test_home_navigation_to_timeline(browser):
    browser.get(BASE_URL)
    browser.find_element(By.LINK_TEXT, "Timeline").click()
    assert "timeline" in browser.current_url.lower()


def test_home_navigation_to_guided_tour(browser):
    browser.get(BASE_URL)
    browser.find_element(By.LINK_TEXT, "Guided Tour").click()
    assert "guided" in browser.current_url.lower()