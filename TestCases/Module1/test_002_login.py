from TestCases.Base_Test import BaseTest
from POM.Login_Page import LoginPage


class Testlogin(BaseTest):

    def test_001(self):
        lg = LoginPage(self.driver)
        lg.navigate_to_tab_login()
        lg.enter_user_name()
        lg.enter_password()
        lg.click_login()


