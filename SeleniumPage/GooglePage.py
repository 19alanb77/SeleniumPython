'''
Created on 20 sty 2020

@author: alan.buda
'''

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class GooglePage():
            
    def __init__(self, driver):
        self.driver = driver
        
        self.searchbox_name = "q"
        self.google_address = "http://www.google.pl"
        self.searched_result_xpath = "(//h3)[1]"
        
        
    def open_page(self):
        driver = self.driver
        driver.get(self.google_address)
        
    def search_result(self, word):
        driver = self.driver
        driver.find_element_by_name(self.searchbox_name).send_keys(word)
        driver.find_element_by_name(self.searchbox_name).send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(self.searched_result_xpath))
        
    def open_first_result(self):
        driver = self.driver
        driver.find_element_by_xpath(self.searched_result_xpath).click()
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(self.cookie_button))
