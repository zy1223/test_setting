import sys, os


sys.path.append(os.getcwd())


from base.get_driver import get_driver
from base.page import Page





class TestSet(object):
    def setup_class(self):
        self.driver = get_driver('com.android.settings', '.Settings')
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_network(self):
        self.page.set_page().click_more_btn()
        self.page.more_page().click_mobile_btn()
        self.page.mobile_page().select_2G()
        assert '2G' in self.page.mobile_page().get_summary_ret_list()
