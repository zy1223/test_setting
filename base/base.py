from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, driver):
        # 传入驱动对象
        self.driver = driver

    def get_element(self, location, timeout=10, poll=1.0):
        """
        定位单个元素的方法
        :param location: 元组（元素定位类型，类型的属性值）
        :param timeout: 超时时长，默认10s
        :param poll: 间隔时长，默认1.0s
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*location))

    def get_elements(self, location, timeout=10, poll=1.0):
        """
        定位一组元素的方法
        :param location: 元组（元素定位类型，类型的属性值）
        :param timeout: 超时时长，默认10s
        :param poll: 间隔时长，默认1.0s
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*location))

    def click_element(self, location):
        """点击元素"""
        self.get_element(location).click()

    def send_mes_to_element(self, location, text):
        """输入元素"""
        self.get_element(location).clear()
        self.get_element(location).send_keys(text)
