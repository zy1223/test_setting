"""页面元素"""
from selenium.webdriver.common.by import By


class PageElements(object):
    """设置页面 """
    set_search_btn_ID = (By.ID, 'com.android.settings:id/search')  # 搜索按钮
    set_search_bar_ID = (By.ID, 'android:id/search_src_text')  # 搜索输入框
    set_search_ret_ID = (By.ID, 'com.android.settings:id/title')  # 搜索结果列表
    set_more_btn_XPATH = (By.XPATH, '//*[contains(@text,"更多")]')  # 更多按钮
    """更多页面"""
    more_mobile_btn_XPATH = (By.XPATH, '//*[contains(@text,"移动网络")]')  # 移动网络
    """移动网络设置页面"""
    mobile_one_net_XPATH = (By.XPATH, '//*[contains(@text,"首选网络类型")]')  # 首选网络类型
    mobile_2G_btn_XPATH = (By.XPATH, '//*[contains(@text,"2G")]')  # 2G
    mobile_summary_ret_ID = (By.ID, 'android:id/summary')  # summary结果列表
