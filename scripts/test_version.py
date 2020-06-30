from base.base_driver import init_driver
from page.page import Page


class TestVersion:
    def teardown(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def test_version(self):
        self.page.my.setting()
        self.page.setting.version()
        self.page.about.click_update()
        assert self.page.about.is_toast_exist("当前已是最新版本")