from POM import *
from POM.Register_Page import Register
from TestCases import *

class TestLogin(BaseTest):

    def __init__(self):
        global setup
        setup = BaseTest()
        setup.setUp()
        self.register = Register_Page(setup.driver)

    def test1_01(self):
        print("Running Login")
        self.register.enter_user_name()

obj = TestLogin()
obj.test_01()