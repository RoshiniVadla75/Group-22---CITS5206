import os
import sys
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from werkzeug.serving import make_server

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from app import create_app
from models import db
import init_db


class ServerThread(threading.Thread):
    def __init__(self, app, host="127.0.0.1", port=5001):
        super().__init__(daemon=True)
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
        self.ctx.pop()


def test_search_page_filtering(tmp_path):
    db_path = tmp_path / "test.db"

    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
    })

    with app.app_context():
        db.drop_all()
        db.create_all()
        init_db.seed_database()

    server = ServerThread(app, port=5001)
    server.start()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("http://127.0.0.1:5001/search")

        search_input = wait.until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )
        empty_state = wait.until(
            EC.presence_of_element_located((By.ID, "emptyState"))
        )
        result_count = wait.until(
            EC.presence_of_element_located((By.ID, "resultCount"))
        )

        assert empty_state.is_displayed()

        driver.execute_script("""
            arguments[0].value = 'Turing';
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        """, search_input)

        wait.until(
            lambda d: len(
                [c for c in d.find_elements(By.CLASS_NAME, "result-card") if c.is_displayed()]
            ) > 0
        )

        visible_cards = [
            c for c in driver.find_elements(By.CLASS_NAME, "result-card")
            if c.is_displayed()
        ]

        assert len(visible_cards) >= 1
        assert any("Turing" in c.text for c in visible_cards)

        driver.execute_script("""
            arguments[0].value = 'zzzzzzz';
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        """, search_input)

        wait.until(
            lambda d: "No results found" in d.find_element(By.ID, "emptyState").text
        )

        driver.execute_script("""
            arguments[0].value = '';
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        """, search_input)

        wait.until(
            lambda d: "Enter a search term" in d.find_element(By.ID, "emptyState").text
        )

    finally:
        driver.quit()
        server.shutdown()