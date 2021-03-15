
from POM import *
from POM.Register_Page import Register
from TestCases import *

class TestLogin(BaseTest):

    def __init__(self):
        base = BaseTest()
        base.setUp()
        self.driver=base.driver

    def testd_01(self):
        print("Running Login")
        rg = Register_Page(self.driver)
        rg.enter_user_name()
        rg.choose_gender()

obj = TestLogin()
obj.test_01()