from base.base import Base
from page.page_elements import PageElements


class MobilePage(Base):
    def __init__(self, driver):
        """继承Base类"""
        Base.__init__(self, driver)

    def select_2G(self):
        """选择2G"""
        self.click_element(PageElements.mobile_one_net_XPATH)
        self.click_element(PageElements.mobile_2G_btn_XPATH)

    def get_summary_ret_list(self):
        ret = self.get_elements(PageElements.mobile_summary_ret_ID)
        return [i.text for i in ret]
