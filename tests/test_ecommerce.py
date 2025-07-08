import unittest
from selenium import webdriver
from pages.home_page import HomePage
import os

class EcommerceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home = HomePage(self.driver)
        self.home.load()

    def test_homepage_logo_visible(self):
        self.assertTrue(self.home.is_logo_visible(), "❌ Logo not visible")

    def test_add_to_cart(self):
        self.home.click_first_product()
        self.home.add_to_cart()
        alert_text = self.home.wait_for_alert_and_accept()
        self.assertIn("Product added", alert_text) 

    def tearDown(self):
        def check_failure_and_screenshot():
            outcome = self._outcome
            if hasattr(outcome, 'errors'):
                errors = outcome.errors
            else:
                result = getattr(outcome, 'result', None)
                if result and (result.failures or result.errors):
                    if not os.path.exists("screenshots"):
                        os.makedirs("screenshots")
                    filepath = f"screenshots/{self._testMethodName}.png"
                    self.driver.save_screenshot(filepath)
                    print(f"📸 Screenshot saved: {filepath}")

        self.addCleanup(check_failure_and_screenshot)
        self.driver.quit()

if __name__ == "__main__":
    import HtmlTestRunner
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='reports',
            report_title='Ecommerce Selenium Test Report',
            report_name='ecommerce_test_report',
            combine_reports=True,
            add_timestamp=True
        )
    )
