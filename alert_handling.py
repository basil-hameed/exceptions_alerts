from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep

class Data:
    url = "https://qavbox.github.io/demo/alerts/"
    my_name = 'basil ahamed'

class Locators:
    alert_button_locator = '//input[@name="commit"]'
    prompt_button_locator = 'prompt'
    confirm_button_locator = 'confirm'

class AlertsHandling(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)

    def simple_alert_box(self):
        try:
            self.start()
            self.driver.find_element(by=By.XPATH, value=self.alert_button_locator).click()
            alert_window = self.driver.switch_to.alert
            alert_window.accept()
            print("SUCCESS : OK button clicked !")
        except (NoAlertPresentException, NoSuchElementException, ElementNotVisibleException) as error:
            print("Error :", error)
        finally:
            self.driver.quit()

    def prompt_alert(self):
        try:
            self.start()
            self.driver.find_element(by=By.ID, value=self.prompt_button_locator).click()
            alert_window = self.driver.switch_to.alert
            alert_window.send_keys(self.my_name)
            alert_window.accept()
            sleep(3)
            print("SUCCESS :  Handled alert prompt successfully !")
        except (NoAlertPresentException, NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR : ", error)
        finally:
            self.driver.quit()

    def confirmation_alert(self):
        try:
            self.start()
            self.driver.find_element(by=By.ID, value=self.confirm_button_locator).click()
            alert_window = self.driver.switch_to.alert
            alert_window.accept()
            sleep(3)
            print("SUCCESS :  Handled confirmation prompt successfully !")
        except (NoAlertPresentException, NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR : ", error)
        finally:
            self.driver.quit()


myAlerts = AlertsHandling()
myAlerts.simple_alert_box()
myAlerts.prompt_alert()
myAlerts.confirmation_alert()