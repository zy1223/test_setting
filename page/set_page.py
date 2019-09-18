from base.base import Base
from page.page_elements import PageElements


class SetPage(Base):
    def __init__(self, driver):
        """继承Base类"""
        Base.__init__(self, driver)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_element(PageElements.set_search_btn_ID)

    def click_more_btn(self):
        """点击更多按钮"""
        self.click_element(PageElements.set_more_btn_XPATH)

    def input_mes_search_bar(self, text):
        # 输入内容
        self.send_mes_to_element(PageElements.set_search_bar_ID, text)

    def get_search_ret_list(self):
        # 获取结果列表
        ret = self.get_elements(PageElements.set_search_ret_ID)
        return [i.text for i in ret]
