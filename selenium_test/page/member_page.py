import time

from test_pytest.selenium_test.page.base_page import BasePage


class MemberPage(BasePage):
    def setup(self):
        pass

    def add_save_member(self):
        self.find_by_css("#username").send_keys(self.add_member_name_info())  # 输入名字
        self.find_by_css("#memberAdd_acctid").send_keys(self.add_member_account_info())  # 输入账号
        self.find_by_css("#memberAdd_phone").send_keys(self.add_member_phone_info())  # 输入 手机号码
        self.find_by_css("#memberAdd_title").send_keys(self.add_member_position_info())  # 输入职务
        self.find_by_path("//*[@class='member_colRight_operationBar ww_operationBar'][1]/a[2]").click()  # 点击保存
        time.sleep(2)

    def delete_member(self):
        self.find_by_path("//*[@id='member_list']/tr[3]/td/input").click()  # 点击第三个选择按钮
        self.find_by_path("//*[@class='ww_operationBar']/a[3]").click()  # 点击删除按钮
        self.find_by_path("//*[@d_ck='submit']").click()  # 点击确定按钮
        time.sleep(2)
