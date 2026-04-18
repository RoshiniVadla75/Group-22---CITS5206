from selenium.webdriver.common.by import By


def test_home_page_loads(driver, base_url):
    driver.get(base_url)

    # Check page title
    assert "Home" in driver.title or "Museum" in driver.title


def test_home_navbar_links(driver, base_url):
    driver.get(base_url)

    # Check navbar links exist
    assert driver.find_element(By.LINK_TEXT, "Home")
    assert driver.find_element(By.LINK_TEXT, "Timeline")
    assert driver.find_element(By.LINK_TEXT, "Guided Tour")


def test_home_navigation_to_timeline(driver, base_url):
    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "Timeline").click()

    assert "timeline" in driver.current_url.lower()


def test_home_navigation_to_guided_tour(driver, base_url):
    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "Guided Tour").click()

    assert "guided" in driver.current_url.lower()


def test_home_page_content_present(driver, base_url):
    driver.get(base_url)

    # Example: check heading exists (adjust based on your HTML)
    body = driver.find_element(By.TAG_NAME, "body")
    assert body is not None