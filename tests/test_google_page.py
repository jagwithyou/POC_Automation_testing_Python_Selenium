
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
from page_objects.google_page import GooglePage
from utility.BaseClass import BaseClass

class TestGooglePage(BaseClass):
    def test_google_search(self):
        ''' This is a test case to test the search page of Google '''
        #Instantiating the logger
        log = self.getLogger()
        log.info("Google Search Test Started")
        #Instantiating the page
        google_page= GooglePage(self.driver)
        #accessing the search field and sending jag to that
        google_page.get_search_bar().send_keys('jag')
        #accessing the submit button and clicking it
        google_page.get_submit_button().submit()
        #logging the test success
        log.info("Test Success")

