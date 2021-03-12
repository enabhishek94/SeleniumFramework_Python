from POM import *
from TestCases import *

class TestLogin(BaseTest):

    def __init__(self):
        global setup
        setup = BaseTest()
        setup.setUp()
        self.login_page = Register(setup.driver)

    def test_02(self):
        print("Running Login")
        self.login_page.click_login()

obj = TestLogin()
obj.test_02()