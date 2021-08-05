# 首页的page
from test_pytest.selenium_test.page.base_page import BasePage
from test_pytest.selenium_test.page.department_page import DepartmentPage
from test_pytest.selenium_test.page.member_page import MemberPage


class MainPage(BasePage):
    url = 'https://work.weixin.qq.com/wework_admin/frame'  # 对基类的url进行重写

    def goto_add_member(self):  # 进入添加成员页面
        self.driver.find_element_by_xpath("//*[@node-type='addmember']").click()  # 点击添加成员
        return MemberPage(self.driver)

    def goto_address_book(self):
        self.find_by_css("#menu_contacts").click()  # 进入通讯录页面
        return MemberPage(self.driver)

    def goto_import(self):
        self.driver.find_element_by_xpath("//*[@node-type='import']").click()  # 点击导入通讯录

    def goto_attendance(self):
        self.driver.find_element_by_xpath("//*[@node-type='attendance']").click()  # 点击打卡

    def goto_address_book_department(self):
        self.find_by_css("#menu_contacts").click()  # 进入通讯录-点击添加部门
        return DepartmentPage(self.driver)
