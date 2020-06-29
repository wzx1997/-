from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MyPage(BaseAction):

    my_name_test=By.ID,"com.yunmall.lc:id/tv_user_nikename"

    def my_name(self):
        return self.find_element(self.my_name_test)