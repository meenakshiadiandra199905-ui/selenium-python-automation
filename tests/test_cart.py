# Automation tests for Shopping Cart
import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.logger import get_logger 
from utils.data_reader import get_login_data

@pytest.mark.flaky(reruns=2)
@pytest.mark.smoke
@pytest.mark.parametrize("username, password", get_login_data())
def test_add_product_to_cart(driver, username, password):

    logger = get_logger()

    logger.info("Opening SauceDemo website")
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    cart = CartPage(driver)

    logger.info("Logging in with {username}")
    login.login(username, password)

    print(driver.current_url)

    logger.info("Adding productto cart")
    result = cart.add_product_to_cart()

    assert result, "Product was not added to cart"

    logger.info("Opening cart page")
    cart.open_cart()

    assert "cart" in driver.current_url.lower()

