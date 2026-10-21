"""Seven automated Selenium WebDriver test cases for the local demo shop."""
import os
import unittest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")
SCREENSHOTS = Path(__file__).resolve().parents[1] / "screenshots"

class ShopUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        SCREENSHOTS.mkdir(parents=True, exist_ok=True)

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1366,900")
        if os.getenv("HEADLESS", "0") == "1":
            options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(BASE_URL)

    def tearDown(self):
        try:
            self.driver.save_screenshot(str(SCREENSHOTS / f"{self._testMethodName}.png"))
        finally:
            self.driver.quit()

    def login(self, password="123456"):
        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-btn").click()

    def test_01_login_success(self):
        self.login()
        self.wait.until(EC.visibility_of_element_located((By.ID, "shop-area")))
        self.assertEqual(self.driver.find_element(By.ID, "greeting").text, "student")

    def test_02_login_invalid(self):
        self.login("wrong-password")
        self.assertEqual(self.driver.find_element(By.ID, "login-error").text, "Sai tài khoản hoặc mật khẩu")
        self.assertFalse(self.driver.find_element(By.ID, "shop-area").is_displayed())

    def test_03_search_product(self):
        self.login()
        self.driver.find_element(By.ID, "search").send_keys("mouse")
        self.driver.find_element(By.ID, "search-btn").click()
        results = self.driver.find_elements(By.CSS_SELECTOR, "[data-product]")
        self.assertEqual(len(results), 1)
        self.assertIn("Mouse", results[0].text)

    def test_04_search_missing(self):
        self.login()
        self.driver.find_element(By.ID, "search").send_keys("not-exist")
        self.driver.find_element(By.ID, "search-btn").click()
        self.assertEqual(self.driver.find_element(By.ID, "no-results").text, "Không tìm thấy sản phẩm")

    def test_05_add_to_cart(self):
        self.login()
        self.driver.find_element(By.CSS_SELECTOR, '[data-add="1"]').click()
        self.assertEqual(self.driver.find_element(By.ID, "cart-count").text, "1")
        self.assertIn("Laptop", self.driver.find_element(By.ID, "cart-items").text)

    def test_06_clear_cart(self):
        self.login()
        self.driver.find_element(By.CSS_SELECTOR, '[data-add="2"]').click()
        self.driver.find_element(By.ID, "clear-cart").click()
        self.assertEqual(self.driver.find_element(By.ID, "cart-count").text, "0")
        self.assertEqual(self.driver.find_element(By.ID, "empty-cart").text, "Giỏ hàng trống")

    def test_07_logout(self):
        self.login()
        self.driver.find_element(By.ID, "logout-btn").click()
        self.assertTrue(self.driver.find_element(By.ID, "login-area").is_displayed())
        self.assertFalse(self.driver.find_element(By.ID, "shop-area").is_displayed())

if __name__ == "__main__":
    unittest.main(verbosity=2)
