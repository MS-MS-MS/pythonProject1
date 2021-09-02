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
        self.driver.quit()
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

    @pytest.mark.skip
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
        self.driver.find_element(By.XPATH,"//em[text()='北京']").click()

        self.driver.find_element(By.ID,"work_position_click_bottom_save").click()
        self.driver.find_element(By.XPATH,"//button[text()='搜索']").click()
        """
        在查询页面的数据是要使用find_elements
        要拿到所有数据否则回报错显示 
        TypeError: 'WebElement' object is not iterable 对象不可编辑
        """
        list=self.driver.find_elements_by_css_selector(".j_result>div>div:nth-child(2)>div:nth-child(4)>div:nth-child(1)")
        for data  in list:
            """
            在定位数据中查询所有的span标签
            获取所有span标签中的text属性
            """
            spans = [i.text for i in data.find_elements_by_css_selector("span")]
            print(" | ".join(spans)+"\n")

    def test_51_search(self):
        """
        实战题目
        登录 http://www.51job.com
        点击高级搜索
        输入搜索关键词 python
        地区选择 杭州
        职能类别 选 计算机软件 -> 高级软件工程师
        公司性质 选 上市公司
        工作年限 选 1-3 年
        搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
        Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
        Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
        :return:
        """
        self.driver.get("http://www.51job.com")
        self.driver.find_element(By.CLASS_NAME,"more").click()
        self.driver.find_element(By.ID,"kwdselectid").send_keys("python")
        self.driver.find_element(By.ID,"work_position_input").click()
        self.driver.find_element(By.XPATH,"//em[text()='北京']").click()
        self.driver.find_element(By.XPATH,"//em[text()='杭州']").click()
        self.driver.find_element(By.ID,"work_position_click_bottom_save").click()
        #选择职能泪飙
        self.driver.find_element(By.ID,"funtype_click").click()
        # 点击测试
        self.driver.find_element(By.ID,"funtype_click_center_right_list_category_0100_2700").click()
        # 选择软件工程师
        self.driver.find_element(By.ID,"funtype_click_center_right_list_sub_category_each_0100_2707").click()
        # 点击确定
        self.driver.find_element(By.ID,"funtype_click_bottom_save").click()
        #公司性质
        self.driver.find_element(By.ID,"cottype_list").click()
        #选择上市公司
        self.driver.find_element_by_css_selector("#cottype_list>div>span:nth-child(5)").click()


