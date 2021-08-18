import time

from appium import webdriver
# 用于滑动点击
from appium.webdriver.common.mobileby import MobileBy
# 用于toast提示用的
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWeiChat:
    def setup(self):
        desire_cap = {"platformName": "android",
                      "devicesName": "emulator-5554",
                      "appPackage": "com.tencent.wework",
                      "appActivity": ".launch.WwMainActivity",
                      "platformVersion": "6.0",
                      "noReset": True,  # 不清空缓存启动app
                      "settings[waitForIdleTimeout]": 0,
                      # 加上下面两个参数后可以在文本框中输入中文
                      "unicodeKeyboard": True,
                      "resetKeyboard": True
                      }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_clock_in(self):  # 打卡
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()  # 点击工作台
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()  # 滑动后点击打卡功能
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()  # 点击外出打卡
        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click()  # contains包含次打卡的元素
        els = self.driver.find_element_by_xpath("//*[@text='外出打卡成功']")
        assert els
        print("打卡成功")

    def test_add_member(self):  # 通讯录-添加客户
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()  # 点击通讯录
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()  # 滑动屏幕后点击添加成员
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText[1]").send_keys(
            "张三丰")  # 输入姓名
        self.driver.find_element_by_xpath(
            "//*[contains(@text,'手机')]/../android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.EditText").send_keys(
            "15334345236")  # 输入手机号码
        self.driver.find_element_by_xpath("//*[@text='保存']").click()  # 点击保存
        toast_loc = ("xpath", "//*[@text = '添加成功']")  # 通过xpath找到元素添加成功
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)) # 获取添加成功元素
        assert toast
        print("添加成员成功")