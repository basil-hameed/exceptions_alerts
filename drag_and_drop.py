from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep

# Import the action chains class
from selenium.webdriver.common.action_chains import ActionChains

class Data:
    url = "https://qavbox.github.io/demo/dragndrop/"

class Locators:
    source_element_locator = 'draggable'
    target_element_locator = 'droppable'

class DragandDrop(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.action = ActionChains(self.driver)

    def drag_drop(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            source_element = self.driver.find_element(by=By.ID, value=self.source_element_locator)
            target_element = self.driver.find_element(by=By.ID, value=self.target_element_locator)

            # using action chain for performing drag and drop
            self.action.drag_and_drop(source_element, target_element).perform()
            print("SUCCESS : Drag and Drop !")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("Element is not visible !", error)
        finally:
            self.driver.quit()

myActions = DragandDrop()
myActions.drag_drop()




