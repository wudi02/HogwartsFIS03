from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.selenium_po.page.add_member_page import AddMemberPage
from test_selenium.selenium_po.page.basepage import BasePage
from test_selenium.selenium_po.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact_page(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member_page(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap .index_service_cnt_item").click()
        return AddMemberPage(self.driver)
