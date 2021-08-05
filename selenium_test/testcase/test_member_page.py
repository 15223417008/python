import time

from test_pytest.selenium_test.page.main_page import MainPage


class TestMain:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.quit()

    def test_goto_add_member(self):  # 测试随机添加成员
        self.main.goto_add_member().add_save_member()  # 添加成员
        save_success = self.main.find_by_css("#js_tips")  # 找到页面添加成功元素：保存成功
        if save_success:  # 判断是否有该元素
            print("添加成员成功")
        else:
            print("添加成员失败")

    def test_add_department(self):  # 测试随机添加部门
        self.main.goto_address_book_department().add_department()
        add_department_syccess = self.main.find_by_css("#js_tips")  # 找到页面添加部门成功后页面的"从其他部门移入"按钮元素
        if add_department_syccess:  # 判断是否有该元素
            print("添部门加成功")
        else:
            print("添加部门失败")

    def test_delete_member(self):  # 测试删除成员
        self.main.goto_address_book().delete_member()  # 删除成员
        delete_success = self.main.find_by_path("//*[@id='js_tips']")  # 找到删除成功的元素
        if delete_success:  # 判断是否有该元素
            print("删除成员成功")
        else:
            print("删除成员失败")

    def test_delete_department(self):  # 测试删除部门
        self.main.goto_address_book_department().delete_department()  # 删除部门
        delete_department = self.main.find_by_css("#js_tips")  # 找到删除部门成功的元素
        if delete_department:  # 判读是否有该元素
            print("删除部门成功")
        else:
            print("删除部门失败")
