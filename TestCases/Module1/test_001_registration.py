from TestCases.Base_Test import BaseTest
from POM.Register_Page import RegisterPage
import pytest

class TestRegistration(BaseTest):

  #  @pytest.mark.Smoke
    def test_001(self):
        rg = RegisterPage(self.driver)
        rg.enter_user_name()
        rg.choose_gender()

  #  @pytest.mark.Sanity
    def test_002(self):
        rg = RegisterPage(self.driver)
        rg.enter_user_name()
        rg.choose_gender()

    @pytest.mark.smoke
    def test_003(self):
        rg =RegisterPage(self.driver)
        rg.scroll_down()


