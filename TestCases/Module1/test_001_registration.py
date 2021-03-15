from TestCases.Base_Test import BaseTest
from POM.Register_Page import RegisterPage


class TestRegistration(BaseTest):

    def test_001(self):
        rg = RegisterPage(self.driver)
        rg.enter_user_name()
        rg.choose_gender()


