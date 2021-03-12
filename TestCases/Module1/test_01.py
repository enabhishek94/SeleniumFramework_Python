from POM import *
from TestCases import *

class TestLogin(BaseTest):

    def __init__(self):
        global setup
        setup = BaseTest()
        setup.setUp()
        self.login_page = Register(setup.driver)

    def test_01(self):
        print("Running Login")
        self.login_page.enter_user_name()

obj = TestLogin()
obj.test_01()