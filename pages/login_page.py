import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from random_word import RandomWords


class LoginPage(BasePage):
    def __init__(self, browser: WebDriver, url, timeout=10):
        super().__init__(browser, url, timeout)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, "Url is not corrected"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        registration_email.send_keys(email)
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        registration_password.send_keys(password)
        registration_password_confirm = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD)
        registration_password_confirm.send_keys(password)
        registration_button_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_CONFIRM)
        registration_button_confirm.click()
