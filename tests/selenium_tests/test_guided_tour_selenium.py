import uuid

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "http://127.0.0.1:5000"


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1400,1000")
    return webdriver.Chrome(options=chrome_options)


def signup_test_user(driver, wait):
    unique_id = uuid.uuid4().hex[:8]
    email = f"guidedtour_{unique_id}@example.com"
    username = f"guidedtour_{unique_id}"
    password = "Password123!"

    driver.get(f"{BASE_URL}/signup")

    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    wait.until(EC.presence_of_element_located((By.NAME, "email")))
    wait.until(EC.presence_of_element_located((By.NAME, "password")))
    wait.until(EC.presence_of_element_located((By.NAME, "confirm_password")))

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "confirm_password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # signup 成功后，理论上会 redirect 到 home
    wait.until(lambda d: "/signup" not in d.current_url)

    return email, password


def test_guided_tour_page_flow():
    driver = create_driver()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Sign up a fresh user
        signup_test_user(driver, wait)

        # 2. Open guided tour page
        driver.get(f"{BASE_URL}/guided-tour")

        # 3. Confirm we are not redirected to login
        wait.until(lambda d: "/login" not in d.current_url)

        # 4. Wait for Guided Tour app container
        guided_app = wait.until(
            EC.presence_of_element_located((By.ID, "guidedTourApp"))
        )
        assert guided_app is not None

        page_source = driver.page_source
        assert "Guided Tour" in page_source or "Begin Journey" in page_source

        # 5. Click Begin Journey
        begin_button = wait.until(
            EC.element_to_be_clickable((By.ID, "beginJourneyBtn"))
        )
        begin_button.click()

        # 6. Verify navigation controls appear
        next_button = wait.until(
            EC.presence_of_element_located((By.ID, "nextBtn"))
        )
        prev_button = wait.until(
            EC.presence_of_element_located((By.ID, "prevBtn"))
        )

        assert next_button.is_displayed()
        assert prev_button.is_displayed()

        # first step usually has previous disabled
        assert prev_button.get_attribute("disabled") is not None

        # 7. Verify full exhibit link exists
        page_text = driver.page_source
        assert (
            "Open Full Exhibit" in page_text
            or "Inspect Full Artefact Detail" in page_text
            or "/topic/" in page_text
        )

        # 8. Move to next topic
        next_button.click()

        wait.until(lambda d: d.find_element(By.ID, "prevBtn").is_displayed())
        prev_button = driver.find_element(By.ID, "prevBtn")
        assert prev_button.is_displayed()

        # 9. Move back
        prev_button.click()

        # 10. Progress dots should exist
        progress_dots = driver.find_elements(By.CLASS_NAME, "progress-dot")
        assert len(progress_dots) > 0

    finally:
        driver.quit()