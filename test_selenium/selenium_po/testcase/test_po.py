import os

import pytest
import yaml

from test_selenium.selenium_po.page.main_page import MainPage

yaml_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\datas\member.yaml"
with open(yaml_file_path) as f:
    data = yaml.safe_load(f)
    member = data['member']['datas']


class TestLogin:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,mail", [("lisi", "lisi", "lisi@qq.com")])
    def test_login(self, name, id, mail):
        namelist = self.main.goto_contact_page().click_addmember().add_member(name, id, mail).get_member()
        print(namelist)
        assert name in namelist

    @pytest.mark.parametrize("name,id,mail", member)
    def test_login2(self, name, id, mail):
        namelist2 = self.main.goto_add_member_page().add_member().get_member()
        print(namelist2)
        assert name in namelist2
