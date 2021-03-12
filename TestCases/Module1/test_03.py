from POM import *
from TestCases import *

class TestLogin(BaseTest):

    def __init__(self):
        global setup
        setup = BaseTest()
        setup.setUp()
        self.login_page = LoginPage(setup.driver)

    def test_03(self):
        print("Running Login")
        self.login_page.navigate_to_tab_login()
        self.login_page.enter_user_name()
        self.login_page.enter_password()
        self.login_page.click_login()

obj = TestLogin()
obj.test_03()