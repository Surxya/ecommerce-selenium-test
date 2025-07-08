from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demoblaze.com/"
        self.logo_locator = (By.ID, "nava")

    def load(self):
        self.driver.get(self.url)

    def is_logo_visible(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.logo_locator)
        )
        return self.driver.find_element(*self.logo_locator).is_displayed()

    def click_first_product(self):
        first_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='hrefch']"))
        )
        first_product.click()

    def add_to_cart(self):
        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
        )
        add_btn.click()

    def wait_for_alert_and_accept(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

