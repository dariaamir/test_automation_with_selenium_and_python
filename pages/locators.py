from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators ():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators ():
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "product_page")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main H1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    CONFIRMATION_MESSAGE_1 = (By.XPATH, "(//div[@id='messages']//./strong)[1]")
    CONFIRMATION_MESSAGE_2 = (By.XPATH, "(//div[@id='messages']//./strong)[2]")
    CONFIRMATION_MESSAGE_3 = (By.XPATH, "(//div[@id='messages']//./strong)[3]")