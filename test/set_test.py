import sys, os

sys.path.append(os.getcwd())
import pytest, allure

from base.get_driver import get_driver
from base.page import Page
from base.read_data import ReadData


def data_test():
    data1 = ReadData().read_yaml_data('test_data.yml')
    data2 = data1.get('data')
    data_list = []
    for i in data2.keys():
        data_list.append((i, data2.get(i).get('t'), data2.get(i).get('exp')))
    # print(data_list)
    return data_list


class TestSet(object):
    def setup_class(self):
        self.driver = get_driver('com.android.settings', '.Settings')
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    @allure.step('点击搜索')
    def click_set_search_btn(self):
        self.page.set_page().click_search_btn()

    @pytest.mark.parametrize('test_num,text,exp', data_test())
    @allure.step('测试设置搜索')
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_set_search(self, test_num, text, exp):
        allure.attach(test_num, '输入数据：%s,预期：%s' % (text, exp))
        self.page.set_page().input_mes_search_bar(text)
        assert exp in self.page.set_page().get_search_ret_list()
