from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators ():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_FORM_EMAIL_INPUT = (By.CSS_SELECTOR, "#register_form input[name=registration-email]")
    REGISTER_FORM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#register_form input[name=registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#register_form input[name=registration-password2]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators ():
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "product_page")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main H1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    CONFIRMATION_MESSAGES = (By.CSS_SELECTOR, "#messages .alert") # this is main selector for all confirmation messages
    CONFIRMATION_MESSAGE_1 = (By.XPATH, "(//div[@id='messages']//./strong)[1]")
    CONFIRMATION_MESSAGE_2 = (By.XPATH, "(//div[@id='messages']//./strong)[2]")
    CONFIRMATION_MESSAGE_3 = (By.XPATH, "(//div[@id='messages']//./strong)[3]")

class BasketPageLocators ():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket_summary .basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner p")