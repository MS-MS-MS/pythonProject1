# -*- coding: utf-8 -*-
""" 
@Time    : 2021/9/1 10:50
@Author  : MaSai
@FileName: test_webui.py
@SoftWare: PyCharm
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_WebUI:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        # self.driver.quit()
        pass
    @pytest.mark.skip
    def test_weibo(self):
        """
        实战题目
        访问：https://m.weibo.cn/
        点击：大家都在搜
        点击：微博热搜榜
        找到：实时热点，每分钟更新一次
        将其中带有 热、沸、新字样的热搜信息获取到，并注明属于三种当中的哪一种
        """
        self.driver.get("https://m.weibo.cn/")
        self.driver.find_element_by_css_selector(".m-text-cut").click()
        # time.sleep(2)
        self.driver.find_element_by_css_selector(".card-main>div:nth-child(10)>div>div>h4").click()
        lists = self.driver.find_element_by_class_name("card11").find_element_by_class_name(
            "card-list").find_elements_by_class_name("card4")
        print(lists)

        # 循环热搜列表
        for i in lists:
            text = i.find_element_by_class_name("main-text").text
            span = i.find_elements_by_class_name("m-link-icon")
            if span:
                src = span[0].find_element_by_tag_name("img").get_attribute("src")

                if "hot" in src:
                    print(f"{text} 是 很热的头条")
                elif "new" in src:
                    print(f"{text} 是 新的头条")
                elif "fei" in src:
                    print(f"{text} 是 沸腾的头条")
                elif "recom" in src:
                    print(f"{text} 是 推荐的头条")
                else:
                    print(f"{text} 是 普通的头条")
    @pytest.mark.skip
    def test_toutiao(self):
        """
        实战题目
        访问：https://www.toutiao.com/
        获取到下图所有黑框里的内容并打印出来
        """
        self.driver.get("https://www.toutiao.com/")
        # action=ActionChains(self.driver)
        # loactor=(By.CSS_SELECTOR,".feed-m-nav>ul>li:nth-child(8)>div>a")
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(loactor))
        # self.driver.find_element_by_css_selector(".feed-m-nav>ul>li:nth-child(8)>div>a").click()
        # move=self.driver.find_element_by_css_selector(".feed-m-nav>ul>li:nth-child(9)")
        self.driver.find_element_by_css_selector(".search").send_keys("sss")
        # print(move)
        # # # 光标移动
        # action.move_to_element(move)
        # # 执行
        # action.perform()
        # time.sleep(5)

    def test_51(self):
        """
        实战题目
        1、访问：http://www.51job.com
        2、输入搜索关键词 "python"， 地区选择 "北京"（注意，如果所在地已经选中其他地区，要去掉）
        3、搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
        Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
        Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
        高级Python开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27
        :return:
        """
        self.driver.get("http://www.51job.com")
        #输入python
        self.driver.find_element(By.XPATH,"//*[@id='kwdselectid']").send_keys("python")\
        # 切换城市
        self.driver.find_element(By.ID,"work_position_click").click()
        # 取消默认定位城市
        self.driver.find_element(By.ID,"work_position_click_ip_location_000000_010000").click()
        # 选择城市
        self.driver.find_element(By.XPATH,"//em[text()='杭州']").click()

        self.driver.find_element(By.ID,"work_position_click_bottom_save").click()
        self.driver.find_element(By.XPATH,"//button[text()='搜索']").click()
        # time.sleep(5)

        # 设置元素等待实例，最多等10秒，每0.5秒查找一次
        def wait_elements(driver, by_, element_, timeout=10):
            element = WebDriverWait(driver=driver, timeout=timeout).until(
                lambda x: x.find_elements(by=by_, value=element_)
            )
            return element
            # 找到职位列表
        lists = wait_elements(self.driver, By.CSS_SELECTOR, "div#resultList>div.el")[1:]

        for data in lists:
            spans = [i.text for i in data.find_elements_by_css_selector("span")]
            print(" | ".join(spans))

    @pytest.mark.skip
    def test_a(self):
        from time import sleep
        from selenium import webdriver
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.common.by import By

        # 设置元素等待实例，最多等10秒，每0.5秒查找一次
        def wait_element(driver, by_, element_, timeout=10):
            element = WebDriverWait(driver=driver, timeout=timeout).until(
                lambda x: x.find_element(by=by_, value=element_)
            )
            return element

        # 设置元素等待实例，最多等10秒，每0.5秒查找一次
        def wait_elements(driver, by_, element_, timeout=10):
            element = WebDriverWait(driver=driver, timeout=timeout).until(
                lambda x: x.find_elements(by=by_, value=element_)
            )
            return element

        # 加载驱动
        driver = webdriver.Chrome("../resources/chromedriver.exe")

        # 打开网站
        driver.get("http://www.51job.com")
        driver.maximize_window()
        # 搜索框
        wait_element(driver, By.CSS_SELECTOR, "#kwdselectid").send_keys("python")

        # 地区按钮
        wait_element(driver, By.CSS_SELECTOR, "#work_position_input").click()

        # 热门城市列表
        city_lists = wait_elements(driver, By.CSS_SELECTOR, "div#work_position_click_center_right_list_000000 td em.on")

        # 选中北京，取消选中其他城市
        for city in city_lists:
            sleep(1)
            city.click()

        wait_element(driver, By.CSS_SELECTOR, "em#work_position_click_center_right_list_category_000000_010000").click()

        # 确定按钮
        driver.find_element_by_css_selector("#work_position_click_bottom_save").click()

        # 搜索按钮点击
        wait_element(driver, By.CSS_SELECTOR, "div.top_wrap button").click()

        # 找到职位列表
        lists = wait_elements(driver, By.CSS_SELECTOR, "div#resultList>div.el")[1:]

        for data in lists:
            spans = [i.text for i in data.find_elements_by_css_selector("span")]
            print(" | ".join(spans))

        sleep(10)
        # 退出浏览器
        driver.quit()