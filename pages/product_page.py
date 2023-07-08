from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_product_description()

    def should_be_product_url(self):
        current_url = self.browser.current_url
        assert 'catalogue' in current_url, "Product page URL is not correct"

    def should_be_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), \
            "Product Description is not presented"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_confirmation_message_1_text(self):
        return self.browser.find_element(*ProductPageLocators.CONFIRMATION_MESSAGE_1).text

    def get_confirmation_message_2_text(self):
        return self.browser.find_element(*ProductPageLocators.CONFIRMATION_MESSAGE_2).text

    def get_confirmation_message_3_text(self):
        return self.browser.find_element(*ProductPageLocators.CONFIRMATION_MESSAGE_3).text

    def add_product_to_basket(self):
        WebDriverWait(self.browser, 5).until(ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET_BUTTON))
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def procuct_name_in_confirmation_message_should_be_correct(self):
        product_name = self.get_product_name()
        confirmation_message_1_text = self.get_confirmation_message_1_text()
        assert product_name == confirmation_message_1_text, \
            f"Product name is not present in confirmation message. " \
            f"Actual: {confirmation_message_1_text}, expected {product_name}"

    def product_price_in_confirmation_message_should_be_correct(self):
        product_price = self.get_product_price()
        confirmation_message_3_text = self.get_confirmation_message_3_text()
        assert product_price in confirmation_message_3_text, \
            f"Product price is not present in confirmation message. " \
            f"Actual: {confirmation_message_3_text}, expected {product_price}"

    def success_message_should_not_be_present(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRMATION_MESSAGES), \
            "When adding product to basket, confirmation message is displayed"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRMATION_MESSAGES), \
            "When adding product to basket, confirmation message does not dissapear"