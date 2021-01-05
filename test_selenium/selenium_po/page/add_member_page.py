from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.selenium_po.page.basepage import BasePage
from test_selenium.selenium_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _ele_name = (By.ID, "username")
    _ele_id = (By.ID, "memberAdd_acctid")
    _ele_mail = (By.ID, "memberAdd_mail")

    def add_member(self, name, id, mail):
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_mail).send_keys(mail)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self, name, id, mail):
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_mail).send_keys(mail)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)
