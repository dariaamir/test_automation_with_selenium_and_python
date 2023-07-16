import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

product_page_without_promo_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
product_page_with_promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
login_page_link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


@pytest.mark.guest
class TestGuestGoToProductPage:
    def test_guest_can_go_to_product_page(self, browser):
        product_page = ProductPage(browser, product_page_with_promo_link)
        product_page.open()
        product_page.should_be_product_page()


@pytest.mark.guest
class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    @pytest.mark.parametrize('link_id', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail),8])
    def test_guest_can_add_product_to_basket(self, browser, link_id):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_id}"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.procuct_name_in_confirmation_message_should_be_correct()
        product_page.product_price_in_confirmation_message_should_be_correct()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self,browser):
        product_page = ProductPage(browser, product_page_with_promo_link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.success_message_should_not_be_present()


@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, email, password):
        login_page = LoginPage(browser, login_page_link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.user_should_be_logged_in()
        yield

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_page_with_promo_link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.procuct_name_in_confirmation_message_should_be_correct()
        product_page.product_price_in_confirmation_message_should_be_correct()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_page_with_promo_link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.success_message_should_not_be_present()


@pytest.mark.guest
def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, product_page_without_promo_link)
    product_page.open()
    product_page.success_message_should_not_be_present()


@pytest.mark.guest
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_page_without_promo_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.success_message_should_disappear()


@pytest.mark.guest
def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, product_page_without_promo_link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.guest
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    product_page = ProductPage(browser, product_page_without_promo_link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.guest
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, product_page_without_promo_link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.basket_should_be_empty()
    basket_page.empty_basket_message_should_be_present_in_empty_basket()
