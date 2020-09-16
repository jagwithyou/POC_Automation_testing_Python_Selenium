from locator.locator import *
from page_objects import BasePage

class GooglePage(BasePage):
    ''' Helps finding all the elements of the page '''
    def get_search_bar(self):
        return self.get_element(GooglePageLocator.SEARCH_BAR)
    
    def get_submit_button(self):
        return self.get_element(GooglePageLocator.SUBMIT_BUTTON)
    
    def get_search_bar_failed(self):
        return self.get_element(GooglePageLocator.SEARCH_BAR_FAILED)