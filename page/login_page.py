from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class LoginPage(BaseAction):

    login_text=By.ID,"com.yunmall.lc:id/textView1"

    def click_login(self):
        self.click(self.login_text)    