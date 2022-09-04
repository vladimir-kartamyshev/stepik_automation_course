from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "items present in basket"

    def should_be_message_basket_is_empty(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY).text
        split_message = message.split(".")
        message_basket_is_empty = split_message[0]
        assert message_basket_is_empty == "Your basket is empty", "Message is not basket is empty"

