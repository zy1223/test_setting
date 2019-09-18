"""获取驱动对象"""
from appium import webdriver


def get_driver(pac, act):
    desired_caps = {}
    # 测试系统
    desired_caps['platformName'] = 'Android'
    # 被测试系统版本
    desired_caps['platformVersion'] = '5.1'
    # 设备名字 随便写 不能为空
    desired_caps['deviceName'] = 'sanxing'
    # 重置键盘
    desired_caps['resetKeyboard'] = True
    # 使用unicode 键盘
    desired_caps['unicodeKeyboard'] = True
    # 设置app包名
    desired_caps['appPackage'] = pac
    # 设置启动名
    desired_caps['appActivity'] = act
    # 声明驱动对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
