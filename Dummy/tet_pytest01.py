from POM import Register_Page
from TestCases.Base_Test import Enviromentstepup


class TestReg(Enviromentstepup):


    def test_001(self):
        lanch = Enviromentstepup()
        lanch.setabc()
        self.driver = lanch.driver
        print(" tc001 Running Login")
        rg = Register_Page(self.driver)
        rg.enter_user_name()
        rg.choose_gender()

    def test_002(self):
        lanch = Enviromentstepup()
        lanch.setabc()
        self.driver = lanch.driver
        print("tc002 Running Login")
        rg = Register_Page(self.driver)
        rg.enter_user_name()
        rg.choose_gender()

test =  TestReg()
test.test_001()
test.test_002()