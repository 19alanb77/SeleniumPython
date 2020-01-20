'''
Created on 20 sty 2020

@author: alan.buda
'''
from selenium import webdriver

import unittest

from SeleniumPage.GooglePage import GooglePage
from SeleniumPage.QAToolsPage import QAToolsPage

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    
    def test_google_search(self):
        driver = self.driver
        googlepage = GooglePage(driver)
        googlepage.open_page()
        googlepage.search_result("automation practice form")
        googlepage.open_first_result()
        
    def test_close_cookies(self):
        driver = self.driver
        toolspage = QAToolsPage(driver)
        assert toolspage.match_title()
        toolspage.close_cookies()
        
    def test_link_table(self):
        driver = self.driver
        toolspage = QAToolsPage(driver)
        toolspage.open_link_table()
        
    def test_subscription(self):
        driver = self.driver
        toolspage = QAToolsPage(driver)
        toolspage.send_email("test@test.pl")
        
    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()