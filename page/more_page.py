from base.base import Base
from page.page_elements import PageElements


class MorePage(Base):
    def __init__(self,driver):
        """继承Base类"""
        Base.__init__(self,driver)

    def click_mobile_btn(self):
        """点击移动网络按钮"""
        self.click_element(PageElements.more_mobile_btn_XPATH)