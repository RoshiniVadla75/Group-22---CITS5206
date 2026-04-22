import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Base URL for the locally running Flask application
BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture
def driver():
    """
    Create and return a Chrome WebDriver instance for each test.
    The browser is maximized to reduce layout issues during testing.
    The driver is automatically closed after each test.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()


def test_timeline_page_title(driver):
    """
    Verify that the Timeline page loads successfully
    and that the browser title is correct.
    """
    driver.get(f"{BASE_URL}/timeline")
    assert "Timeline - AI Museum" in driver.title


def test_timeline_main_heading(driver):
    """
    Verify that the main heading of the Timeline page
    is displayed and matches the expected text.
    """
    driver.get(f"{BASE_URL}/timeline")

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h1.page-title"),
            "Timeline of AI Paradigm Shifts"
        )
    )

    heading = driver.find_element(By.CSS_SELECTOR, "h1.page-title")
    assert heading.text.strip() == "Timeline of AI Paradigm Shifts"


def test_desktop_navigation_exists(driver):
    """
    Verify that the desktop navigation bar is present
    and contains the expected navigation links.
    """
    driver.get(f"{BASE_URL}/timeline")

    nav = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "desktopNav"))
    )

    nav_text = nav.text
    assert "Home" in nav_text
    assert "Timeline" in nav_text
    assert "Guided Tour" in nav_text
    assert "Explore WA" in nav_text
    assert "Search" in nav_text


def test_filter_sections_exist(driver):
    """
    Verify that all filter sections are present on the Timeline page:
    decade filters, category filters, and status filters.
    """
    driver.get(f"{BASE_URL}/timeline")

    decade_filters = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "decadeFilters"))
    )
    category_filters = driver.find_element(By.ID, "categoryFilters")
    status_filters = driver.find_element(By.ID, "statusFilters")

    assert decade_filters.is_displayed()
    assert category_filters.is_displayed()
    assert status_filters.is_displayed()


def test_timeline_list_container_exists(driver):
    """
    Verify that the main timeline list container exists
    and is visible on the page.
    """
    driver.get(f"{BASE_URL}/timeline")

    timeline_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "timelineList"))
    )
    assert timeline_list.is_displayed()


def test_empty_state_hidden_by_default(driver):
    """
    Verify that the empty-state message is hidden by default
    when the page first loads.
    """
    driver.get(f"{BASE_URL}/timeline")

    empty_state = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "emptyState"))
    )

    classes = empty_state.get_attribute("class")
    assert "hidden" in classes