from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        assert 'basket' in current_url, "Basket page URL is not correct"

    def get_list_of_items_in_basket(self):
        return self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)

    def is_basket_empty(self):
        if len(self.get_list_of_items_in_basket()) == 0:
            return True
        else:
            return False

    def basket_should_be_empty(self):
        assert self.is_basket_empty()

    def get_empty_basket_message(self):
        return self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text

    def empty_basket_message_should_be_present_in_empty_basket(self):
        assert "Your basket is empty." in self.get_empty_basket_message(),\
            "Empty basket doesn't have empty basked message"