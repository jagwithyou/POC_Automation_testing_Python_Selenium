from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import config, time

class BasePage(object):
    ''' Base page setup with the driver '''
    def __init__(self, driver):
        self.driver = driver
    
    def get_element(self, element):
        ''' Returns the element by finding from the page
        Parameters:
        element: The element finder tuple eg: (By.NAME,'ELEMENT_NAME') '''
        time.sleep(config.ACTION_DELAY)
        myElem = WebDriverWait(self.driver, config.WEB_DRIVER_WAIT).until(EC.presence_of_element_located(element))
        return myElem