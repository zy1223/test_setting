"""实例化页面类"""
from page.mobile_page import MobilePage
from page.more_page import MorePage
from page.set_page import SetPage


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def set_page(self):
        return SetPage(self.driver)  # 设置页面

    def more_page(self):
        return MorePage(self.driver)  # 更多页面

    def mobile_page(self):
        return MobilePage(self.driver)  # 移动网络页面
