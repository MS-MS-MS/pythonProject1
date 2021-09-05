import re
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Test_WebUI2:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
        pass
    @pytest.mark.skip
    def test_12306(self):
        """
        实战题目
        打开 12306 网站 https://kyfw.12306.cn/otn/leftTicket/init
        出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东'
        发车时间 选 06:00--12:00
        发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
        我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息，结果如下：
        """
        self.driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
        # 关闭弹框
        self.driver.find_element(By.ID,"qd_closeDefaultWarningWindowDialog_id").click()
        # 选择出发城市
        self.driver.find_element(By.ID, "fromStationText").click()
        fromStation=self.driver.find_element(By.ID,"fromStationText")
        fromStation.send_keys("南京南")
        self.driver.find_element_by_css_selector("div#citem_0").click()

        #选择到达城市
        self.driver.find_element(By.ID, "toStationText").click()
        self.driver.find_element(By.ID,"toStationText").send_keys("杭州东")
        self.driver.find_element_by_css_selector("div#citem_0").click()
        # 选择发车时间
        self.driver.find_element(By.ID,"cc_start_time").click()
        # 选择6-12点
        self.driver.find_element(By.CSS_SELECTOR,"#cc_start_time>option:nth-child(3)").click()
        #选择发车日期
        self.driver.find_element(By.CSS_SELECTOR,"#date_range>ul>li:nth-child(2)").click()
        # # 取数据
        # trlist=self.driver.find_elements(By.CSS_SELECTOR,"#queryLeftTable>tr>td:nth-child(4)")
        # for hbdata in trlist:
        #     for i in hbdata.find_elements(By.CSS_SELECTOR,"td"):
        #         print(i.text)
        # 数据列表
        # [0::2] 数据列表中间有一个空值 所以跳过取值
        lists = self.driver.find_elements(By.CSS_SELECTOR, "tbody#queryLeftTable>tr")[0::2]
        print(len(lists))
        #  循环数据
        for data in lists:
            # 查寻列车编号
            number = data.find_element_by_css_selector("td>div>div.train a.number").text
            # 查寻该列车二等座是否票
            two = data.find_elements_by_css_selector("td")[3].text
            # 正则表达是 有是否匹配
            if re.findall("有|\d+", two):
                print(number)

    def test_phone(self):
        '''
        实战题目
        访问: https://www.vmall.com/
        获取一级菜单下包含哪些二级菜单，不包含查看全部
        然后获取下面，热销单品中所有 顶部 带有 爆款字样的产品名称及价格
        '''
        self.driver.get("https://www.vmall.com/")
        action=ActionChains(self.driver)
        ele =self.driver.find_element(By.CSS_SELECTOR,".css-1dbjc4n.r-1awozwy.r-xiad99.r-bnwqim>div:nth-child(2)>div>div>div>div>div>div")
        action.move_to_element(ele)
        action.perform()
        phone_list=self.driver.find_elements(By.CSS_SELECTOR,".r-i023vh")
        for dada in phone_list:
            for i in dada.find_elements(By.CSS_SELECTOR,".r-ezt3gj"):
                print(i.text)

