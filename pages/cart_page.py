from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
       

    def add_product_to_cart(self):
        wait = WebDriverWait(self.driver, 10)

        add_button= wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@id,'add-to-cart')]")
            )
        )
        add_button.click()
        return True

    def open_cart(self):
        wait = WebDriverWait(self.driver, 10)

        cart_icon = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_icon.click()
        
        