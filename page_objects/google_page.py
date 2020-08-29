from locator.locator import *

class BasePage(object):
    ''' Base page setup with the driver '''
    def __init__(self, driver):
        self.driver = driver

class GooglePage(BasePage):
    ''' Helps finding all the elements of the page '''
    def get_search_bar(self):
        return self.driver.find_element(*GooglePageLocator.SEARCH_BAR)
    
    def get_submit_button(self):
        return self.driver.find_element(*GooglePageLocator.SUBMIT_BUTTON)