import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.saucePage import loginPage

def test_baseLoginFailed(self,userinput,passinput,message):
    browser = self.browser
    browser.get('https://www.saucedemo.com/')
    self.assertIn('Swag Labs', self.browser.title)
    browser.find_element(By.NAME, loginPage.user).send_keys(userinput)
    browser.find_element(By.NAME, loginPage.psw).send_keys(passinput)
    browser.find_element(By.ID, loginPage.login_btn).click()
    error_msg = browser.find_element(By.CSS_SELECTOR, loginPage.err_msg).text
    self.assertIn(message, error_msg)
    browser.quit()
