import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.selenium_po.page.basepage import BasePage


class ContactPage(BasePage):
    def click_addmember(self):

        from test_selenium.selenium_po.page.add_member_page import AddMemberPage
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        self.wait_for_click(ele, 5)

        while True:
            # ele = driver.find_element_by_css_selector(".ww_operationBar .js_add_member")
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            # ele.click()
            element = self.finds(By.ID, "username")
            if len(element) > 0:
                break
        return AddMemberPage(self.driver)

    def get_member(self):
        time.sleep(1)
        eles = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in eles:
            print(value.get_attribute("title"))
            name_list.append(value.get_attribute("title"))
        # assert "吴大大8" in name_list
        return name_list
