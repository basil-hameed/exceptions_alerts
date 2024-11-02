from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep

# Action Chains Class
from selenium.webdriver.common.action_chains import ActionChains

class Data:
    url = 'https://demoqa.com/buttons'

class Locators:
    double_click_locator = 'doubleClickBtn'

class DoubleClick(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.action = ActionChains(self.driver)

    def double_click(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            double_click_element = self.driver.find_element(by=By.ID, value=self.double_click_locator)
            self.action.double_click(double_click_element).perform()
            sleep(3)
            print("SUCCESS : Double Clicked !")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR : ", error)
        finally:
            self.driver.quit()

myActions = DoubleClick()
myActions.double_click()