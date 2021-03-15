import unittest
from Library import *
import pytest

class BaseTest(unittest.TestCase):

    def setUp(self):
        print("\n Running setup")
        driver_path = "C:\\Users\\abc\\Desktop\\Python P\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get("https://thetestingworld.com/testings")
        self.driver.maximize_window()

    def tearDown(self):
        print('\n running tear down')
        sw = SeleniumWrapper(self.driver)
        try:
            sw.capture_screen_shot()
        except Exception as e:
            print(e)
        finally:
            self.driver.close()


