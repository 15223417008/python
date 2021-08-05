import time

from test_pytest.selenium_test.page.base_page import BasePage
from selenium.webdriver.support.ui import Select


class DepartmentPage(BasePage):
    def setup(self):
        pass

    def add_department(self):  # 添加部门
        self.find_by_css(".member_colLeft_top_addBtnWrap").click()  # 点击+按钮
        self.find_by_css(".js_create_party").click()  # 点击添加部门
        self.find_by_path("//*[@class='form']/div/input[@name='name']").send_keys(
            self.add_department_name())  # 输入生成的随机部门名称
        self.find_by_path("//*[@class='inputDlg_item'][3]/a").click()  # 点击下拉框
        self.find_by_css("form>div>div>div>ul>li>a").click()  # 点击选择所属部门
        # self.driver.switch_to.alert.accept()  # 点击弹框的确定按钮
        self.find_by_path("//*[@d_ck='submit']").click()  # 点击弹框的确定按钮
        time.sleep(2)

    def delete_department(self):  # 删除部门
        self.find_by_path("//*[@role='group']/li/ul/li[1]").click()
        self.find_by_path("//*[@role='group']/li/ul/li[1]/a/span").click()  # 点击更多按钮
        self.find_by_path(
            "//*[@class='vakata-context jstree-contextmenu jstree-default-contextmenu']/li[7]/a").click()  # 点击删除按钮
        self.find_by_path("//*[@d_ck='submit']").click()  # 点击确定按钮
        time.sleep(2)
