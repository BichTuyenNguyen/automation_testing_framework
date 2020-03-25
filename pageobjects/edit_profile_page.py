from pageobjects.page import BasePage


class EditProfilePage(BasePage):
    def get_user_full_name(self, locator):
        return self.get_element_text(locator)

    def edit_location(self, locator, location):
        self.clear_element_text(locator)
        self.set_element_text(locator, location)

    def get_user_location(self, locator):
        attribute = "value"
        return self.get_attribute_of_element(locator, attribute)
