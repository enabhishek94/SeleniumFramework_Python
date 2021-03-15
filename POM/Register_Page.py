from POM import *
from Library import *
from POM.BasePage import BasePage


class RegisterPage(BasePage):

    Register_Object =read_locators('Register')
    print(Register_Object)

    def enter_user_name(self):
        txt_username = self.__class__.Register_Object['username']
        self.enter_text(txt_username, value='abhishek')

    def click_login(self):
        btn_login = self.__class__.Register_Object['submit']
        self.click_element(btn_login)

    def choose_gender(self):
        value = self.__class__.Register_Object['sex1']
        self.select_list_item(value,item=1)





