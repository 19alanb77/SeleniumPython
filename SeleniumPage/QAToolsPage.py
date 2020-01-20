'''
Created on 20 sty 2020

@author: alan.buda
'''
from selenium.webdriver.support.ui import WebDriverWait

class QAToolsPage:
            
    def __init__(self, driver):
        self.driver = driver
        
        self.cookie_button = "cookie_action_close_header"
        self.link_table = "//a[@title='Automation Practice Table']"
        self.email_input = "email"
        self.subscribe_button = "//input[@value='Subscribe']"
        
        
    def match_title(self):
        return "Demo Form for practicing Selenium Automation" in self.driver.title
        
    def close_cookies(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(self.cookie_button))
        driver.find_element_by_id(self.cookie_button).click()
        
    def open_link_table(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(self.link_table))
        driver.find_element_by_xpath(self.link_table).click() 
    
    def send_email(self,email):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(self.email_input))
        driver.find_element_by_name(self.email_input).send_keys(email)
        driver.find_element_by_xpath(self.subscribe_button).click()