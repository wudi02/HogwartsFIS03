import time

import yaml
from selenium import webdriver


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    # print(driver.get_cookies())
    cookies = driver.get_cookies()
    with open("data.yaml", "w", encoding="utf-8") as f:
        # 序列化cookie，存入yaml文件
        yaml.dump(cookies, f)


class TestDemo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("data.yaml", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="js_contacts47"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        self.driver.find_element_by_link_text("添加成员").click()
        self.driver.find_element_by_id("username").send_keys("吴大大")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("无敌")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("test001")
        self.driver.find_element_by_xpath(
            '//*[@id="js_contacts41"]/div/div[2]/div/div[4]/div/form/div[2]/div[1]/div[3]/div[2]/label[2]/input').click()
        self.driver.find_element_by_id("memberAdd_mail").send_keys("1829739182371987389173@qq.com")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="js_contacts47"]/div/div[2]/div/div[4]/div/form/div[3]/a[1]').click()
        time.sleep(2)

        self.driver.quit()
