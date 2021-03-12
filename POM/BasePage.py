from Library import *

class BasePage(SeleniumWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        print("Base Page")
        self.driver = driver
