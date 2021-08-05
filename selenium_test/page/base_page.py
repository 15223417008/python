# 把selenium的操作，放在基础page中
import secrets

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import random
import string


class BasePage:
    url = 'https://work.weixin.qq.com/'

    def __init__(self, driver: WebDriver = None):  # driver: webdriver=None ：单纯的用于语法提示，本身没有代码功能
        if not driver:  # 如果没有传递driver，说明是第一层调用，比如企业微信官网
            option = Options()
            option.debugger_address = 'localhost:9222'  # 写入启动命令的地址端口
            self.driver = webdriver.Chrome(options=option)
            self.driver.get(self.url) # 定义url，如果子类没有没有重写url，则用父类的url
            self.driver.implicitly_wait(5)
        else:  # 如果传递了driver，说明不是第一次调用，比如企业微信官网->登陆页面
            self.driver = driver

    def quit(self):  # 封装退出浏览器方法
        return self.driver.quit()

    def find_by_css(self, css):  # 封装css定位方法
        return self.driver.find_element_by_css_selector(css)

    def find_by_path(self, path):  # 封装xpath定位方法
        return self.driver.find_element_by_xpath(path)

    def add_member_name_info(self):  # 封装随机生成名字方法
        first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
        second_name = ["伟", "华", "建国", "洋", "刚", "万里", "廷亮", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊",
                       "雷",
                       "文", "明浩", "光", "超", "军", "达", "汪"]
        name = random.choice(first_name) + random.choice(second_name)  # 随机生成名字
        return name

    def add_member_position_info(self):  # 封装随机生成职务方法
        job = ["测试小弟", "测试员", "测试大佬", "开发小弟", "开发大佬", "产品", "视觉", "交互", "项目老大"]
        position = random.choice(job)  # 随机生成职务
        return position

    def add_member_account_info(self):  # 封装随机生成账号方法
        account = ''.join(
            random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=5))  # 随机生成账号
        return account

    def add_member_phone_info(self):  # 封装随机生成手机号码方法
        phone = '15' + str(random.randrange(4, 10)) + ''.join(
            str(random.choice(range(10))) for _ in range(8))  # 随机生成手机号码
        return phone

    def add_department_name(self):  # 封装随机生成随机部门名称
        name1 = ["测试保障", "研发", "产品", "策划", "运营", "营销", "业务", "财务", "法务", "风控", "销售", "后勤"]
        name2 = ["项目组", "部", "科"]

        dpartment_name = random.choice(name1) + random.choice(name2)
        return dpartment_name
