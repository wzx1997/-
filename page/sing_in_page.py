from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class SingInPage(BaseAction):
    account_text = By.ID, "com.yunmall.lc:id/logon_account_textview"
    password_text = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    def input_account(self, text):
        self.input(self.account_text, text)

    def input_password(self, text):
        self.input(self.password_text, text)

    def click_login(self):
        self.click(self.login_button)