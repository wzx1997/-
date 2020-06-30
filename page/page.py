from page.about_page import AboutPage
from page.login_page import LoginPage
from page.main_page import MainPage
from page.my_page import MyPage
from page.setting_page import SettingPage
from page.sing_in_page import SingInPage


class Page:

    def __init__(self,driver):
        self.driver=driver

    @property
    def main(self):
        return MainPage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def my(self):
        return MyPage(self.driver)

    @property
    def sing_in(self):
        return SingInPage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def about(self):
        return AboutPage(self.driver)