import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("test_login.yaml","test_login"))
    def test_login(self,args):
        account=args["account"]
        password=args["password"]
        toast=args["toast"]
        self.page.main.click_me()
        self.page.login.click_login()
        self.page.sing_in.input_account(account)
        self.page.sing_in.input_password(password)
        self.page.sing_in.click_login()
        if toast is None:
            assert self.page.my.my_name() == account
        else:
            assert self.page.sing_in.is_toast_exist(toast)