import pytest
import yaml

from learn_python.work_appium.weixin_PO.page.app import App


class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize("name, gender, phonenum", yaml.safe_load(open("./add_contact.yaml")))
    def test_addcontact(self,name,gender,phonenum):
     result = self.main.goto_contactlist(). \
            add_member().add_member_manul(). \
            edit_contact(name, gender, phonenum).verify_toast()
     assert '添加成功' == result



