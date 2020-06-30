from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SettingPage(BaseAction):
    version_button=By.ID,"com.yunmall.lc:id/setting_about_yunmall"
    def version(self):
        self.find_element_with_scroll(self.version_button).click()