"""
Python - Selenium Exceptions
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Import these exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchDriverException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

class Data:
    url = 'https://suman-dynamic-html-form.netlify.app/'

class Locators:
    first_name_locator = 'fname'

class SeleniumExceptions(Data, Locators):
    def __init__(self):
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        except NoSuchDriverException as error:
            print("ERROR: Python Selenium Driver Not Found!", error)

    def start(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
        except TimeoutException as error:
            print("ERROR: Time Out Error!", error)
    
    def homepage(self):
        try:
            self.start()
            self.driver.find_element(by=By.ID, value=self.first_name_locator)
            print("First Name Element Found !")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR : Element Not Found !", error)
        finally:
            self.driver.quit()

# create an object and call the methods
myException = SeleniumExceptions()
myException.homepage()