from POM import *
from Library import *
from POM.BasePage import BasePage


class LoginPage(BasePage):
    login_objects = read_locators('Login')
    print(login_objects)

    def navigate_to_tab_login(self):
        navigate = self.__class__.login_objects['Navigate_to_logintab']
        self.click_element(navigate)

    def enter_user_name(self):
        txt_username = self.__class__.login_objects['txtUserName']
        self.enter_text(txt_username, value='abhishek')

    def enter_password(self):
        txt_Password = self.__class__.login_objects['txtPassword']
        self.enter_text(txt_Password, value='12345')

    def click_login(self):
        btn_login = self.__class__.login_objects['Login']
        self.click_element(btn_login)
