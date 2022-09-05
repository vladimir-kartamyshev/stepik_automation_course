from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.NAME, "registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD =(By.NAME, "registration-password2")
    REGISTRATION_BUTTON_CONFIRM = (By.NAME, "registration_submit")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] p[class='price_color']")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")
