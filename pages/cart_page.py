from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

time.sleep(2)
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    def is_product_in_cart(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
        )
        return len(items) > 0
            
        
        