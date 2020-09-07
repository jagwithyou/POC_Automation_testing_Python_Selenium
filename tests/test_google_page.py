
from selenium.webdriver.support.select import Select
from page_objects.google_page import GooglePage
from tests import BaseClass
from selenium import webdriver
import pytest, config
from selenium.common.exceptions import NoSuchElementException

class TestGooglePage(BaseClass):
    def test_1_google_search(self):
        ''' This is a test case to test the search page of Google.
        First it open a broeser with url specified in config (Google URL).
        Then it will search for a query.'''
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
        assert True
    
    def test_2_google_search_assertion_failed(self):
        ''' This is the same google search testcase, but it will fail due to assertion error'''
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
        assert False

    def test_3_google_search_element_failed(self):
        ''' This is the same google search testcase, but it will fail due to element not folund error'''
        #Instantiating the logger
        log = self.getLogger()
        log.info("Google Search Test Started")
        #Instantiating the page
        google_page= GooglePage(self.driver)
        #accessing the search field and sending jag to that
        google_page.get_search_bar_failed().send_keys('jag')
        #accessing the submit button and clicking it
        google_page.get_submit_button().submit()
        #logging the test success
        log.info("Test Success")
        assert False
            

