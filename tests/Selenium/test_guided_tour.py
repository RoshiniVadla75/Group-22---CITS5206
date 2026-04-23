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
    wait.until(lambda d: "/signup" not in d.current_url)

    return email, password


def test_guided_tour_page_flow():
    driver = create_driver()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Sign up and log in as a fresh user
        signup_test_user(driver, wait)

        # 2. Open guided tour page
        driver.get(f"{BASE_URL}/guided-tour")

        # 3. Confirm we are not redirected to login
        wait.until(lambda d: "/login" not in d.current_url)

        # 4. Confirm page title
        assert "Guided Tour" in driver.title

        # 5. Wait for the guided tour root container
        guided_app = wait.until(
            EC.presence_of_element_located((By.ID, "guidedTourApp"))
        )
        assert guided_app is not None

        # 6. Wait for dynamic content to be rendered into the app container
        wait.until(
            lambda d: d.execute_script("""
                const root = document.getElementById('guidedTourApp');
                return root && (
                    root.children.length > 0 ||
                    (root.innerText && root.innerText.trim().length > 0)
                );
            """)
        )

        # 7. Verify guided tour content is present
        app_text = driver.execute_script("""
            const root = document.getElementById('guidedTourApp');
            return root ? (root.innerText || root.textContent || '').trim() : '';
        """)

        assert app_text != ""

        # 8. Verify at least one interactive element exists in the guided tour app
        interactive_count = driver.execute_script("""
            const root = document.getElementById('guidedTourApp');
            if (!root) return 0;
            return root.querySelectorAll('button, a, [role="button"], input').length;
        """)

        assert interactive_count > 0

    finally:
        driver.quit()