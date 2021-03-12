from POM import *

class Register(BasePage):
    Register_Object =read_locators()

    def enter_user_name(self):
        #txt_username = self.Register_Object['fld_username']
        txt_username = self.__class__.Register_Object['fld_username']
        self.enter_text(txt_username, value='abhishek')

    def click_login(self):
        btn_login = self.__class__.Register_Object['submit']
        self.click_element(btn_login)




