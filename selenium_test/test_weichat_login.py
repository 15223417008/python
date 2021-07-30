import time
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class TestLogin:
    @pytest.mark.skip
    def test_chrome_remote(self):  # 使用复用浏览器登陆
        option = Options()  # 实例化options
        option.debugger_address = "localhost:9222"  # 写入启动命令的地址端口号
        driver = webdriver.Chrome(options=option)  # 实例化driver，传入option设定的debbuger_address
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 传入企业微信登陆链接
        time.sleep(3)
        # driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click() # 点击通讯录
        # time.sleep(3)
        # driver.find_element_by_xpath("//*[@class='js_operationBar_footer ww_operationBar']/a[1]").click() # 点击添加成员
        driver.find_element_by_css_selector(".index_service_cnt_itemWrap").click()  # 点击添加成员
        time.sleep(3)
        cookie = driver.get_cookies()  # 获取cookie
        yaml.safe_dump(cookie, open("cookie.yaml", mode='w'))  # 把获取到的cookie放到cookie.yaml文件中,写入

    @pytest.mark.skip
    def test_cookie_login(self):  # 使用cookie进行自动登陆
        cookie = yaml.safe_load(open("cookie.yaml", encoding="utf-8"))  # 从cookie.yaml文件中获取cookie
        # print(cookie)
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 打开浏览器
        for cookie_val in cookie:
            driver.add_cookie(cookie_val)  # 将cookie写入浏览器中，由于add每次只能加单个字典，所以需要循环遍历
        time.sleep(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 写入cookie后需要刷新页面
        time.sleep(3)
        driver.find_element_by_css_selector(".index_service_cnt_itemWrap").click()  # 点击添加成员
        time.sleep(3)
    @pytest.mark.skip
    def test_add_member_zhangsan(self):  # 添加成员-张三
        cookie = yaml.safe_load(open("cookie.yaml", encoding="utf-8"))  # 从cookie.yaml文件中获取cookie
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 打开浏览器
        for cookie_val in cookie:
            driver.add_cookie(cookie_val)  # 将cookie写入浏览器中，由于add每次只能加单个字典，所以需要循环遍历
        time.sleep(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 写入cookie后需要刷新页面
        time.sleep(3)
        driver.find_element_by_css_selector(".index_service_cnt_itemWrap").click()  # 点击添加成员
        time.sleep(2)
        driver.find_element_by_css_selector("#username").send_keys("张三")  # 添加成员张三，输入姓名
        time.sleep(1)
        driver.find_element_by_css_selector("#memberAdd_english_name").send_keys("三哥")  # 输入别名
        driver.find_element_by_css_selector("#memberAdd_acctid").send_keys("123456789")  # 输入账号
        driver.find_element_by_css_selector("#memberAdd_phone").send_keys("13333333333")  # # 输入手机号码
        driver.find_element_by_css_selector("#memberAdd_telephone").send_keys("10086")  # 输入座机号码
        driver.find_element_by_css_selector("#memberAdd_mail").send_keys("10086@qq.com")  # 输入邮箱
        driver.find_element_by_css_selector("#memberEdit_address").send_keys("杭州-西湖")  # 输入地址
        time.sleep(2)
        driver.find_element_by_css_selector("#memberAdd_title").send_keys("开发大佬")  # 输入职务
        driver.find_element_by_xpath(
            "//*[@id='js_contacts49']/div/div[2]/div/div[4]/div/form/div[3]/a[2]").click()  # 点击保存
        time.sleep(3)
    def test_add_member_xiaoli(self):  # 添加成员-小李
        cookie = yaml.safe_load(open("cookie.yaml", encoding="utf-8"))  # 从cookie.yaml文件中获取cookie
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 打开浏览器
        for cookie_val in cookie:
            driver.add_cookie(cookie_val)  # 将cookie写入浏览器中，由于add每次只能加单个字典，所以需要循环遍历
        time.sleep(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 写入cookie后需要刷新页面
        time.sleep(3)
        driver.find_element_by_css_selector(".index_service_cnt_itemWrap").click()  # 点击添加成员
        time.sleep(2)
        driver.find_element_by_css_selector("#username").send_keys("小李")  # 添加成员张三，输入姓名
        time.sleep(1)
        driver.find_element_by_css_selector("#memberAdd_english_name").send_keys("李大头")  # 输入别名
        driver.find_element_by_css_selector("#memberAdd_acctid").send_keys("987654321")  # 输入账号
        driver.find_element_by_xpath("//*[@class='member_edit_item_right']//input[@value='2']").click()  # 点击选择女
        time.sleep(1)
        driver.find_element_by_css_selector("#memberAdd_phone").send_keys("16666666666")  # # 输入手机号码
        driver.find_element_by_css_selector("#memberAdd_telephone").send_keys("10010")  # 输入座机号码
        driver.find_element_by_css_selector("#memberAdd_mail").send_keys("10010@qq.com")  # 输入邮箱
        driver.find_element_by_css_selector("#memberEdit_address").send_keys("杭州-滨江")  # 输入地址
        time.sleep(2)
        driver.find_element_by_css_selector("#memberAdd_title").send_keys("测试大佬")  # 输入职务
        driver.find_element_by_xpath("//*[@class='member_edit_item_right']//input[@value='1'][@name='identity_stat']").click()  # 点击选择上级
        driver.find_element_by_xpath("//*[@class='member_colRight_operationBar ww_operationBar'][1]/a[2]").click()  # 点击保存
        time.sleep(3)
