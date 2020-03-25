from pageobjects.page import BasePage


class LoginPage(BasePage):

    def input_user_email(self, locator, email):
        self.set_element_text(locator, email)

    def input_user_password(self, locator, password):
        self.set_element_text(locator, password)

    def go_to_login_page(self, locator):
        self.click_element(locator)


