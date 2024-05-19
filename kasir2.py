import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class KasirTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def test_login_success(self):
        browser = self.driver
        browser.get('https://kasirdemo.belajarqa.com/')
        self.assertIn('kasirAja', browser.title)
        browser.find_element(By.ID, 'email').send_keys('elva@gmail.com')
        browser.find_element(By.ID, 'password').send_keys('elva')
        browser.find_element(By.CSS_SELECTOR, '.chakra-button.css-1n8i4of').click()
        self.assertEqual(browser.current_url, 'https://kasirdemo.belajarqa.com/login')
 
if __name__ == '__main__':
    unittest.main()