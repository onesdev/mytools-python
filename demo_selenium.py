"""
selenium使用练习

selenium是一个自动化测试工具，可以用来模拟用户操作浏览器，自动化测试网站功能。
selenium支持多种浏览器，如Chrome、Firefox、IE、Safari等。
selenium支持多种编程语言，如Python、Java、C#、PHP、Ruby等。
selenium支持多种操作系统，如Windows、Linux、Mac OS等。
selenium支持多种测试框架，如unittest、pytest、nose等。
selenium支持多种测试报告，如HTMLTestRunner、Allure、TestNG等。
selenium支持多种测试工具，如Jenkins、SauceLabs、BrowserStack等。
selenium支持多种测试平台，如Selenium Grid、Appium、Selendroid等。
selenium支持多种测试数据，如Excel、CSV、XML、JSON等。
selenium支持多种测试环境，如Docker、VirtualBox、VMware等。
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 一个简单的百度搜索示例
def open_baidu():
    # 创建浏览器对象，自动下载安装驱动
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # 打开百度首页
    driver.get('https://www.baidu.com')

    # 在搜索框中输入关键字
    search_box = driver.find_element(by=By.NAME, value="wd")
    search_box.send_keys('Python')

    # 点击搜索按钮
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载完成
    time.sleep(5)

    # 输出搜索结果
    results = driver.find_elements(by=By.CSS_SELECTOR, value='.result h3 a')
    for result in results:
        print(result.text)

    # 关闭浏览器
    driver.quit()


# 一个简单的百度搜索示例，使用无界面模式
def open_baidu_headless():
    # 创建浏览器对象，自动下载安装驱动
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # 打开百度首页
    driver.get('https://www.baidu.com')

    # 等待页面加载完成
    time.sleep(5)

    # 输出网页源代码
    print(driver.page_source)

    # 关闭浏览器
    driver.quit()


# 隐式等待示例
def open_baidu_implicitly_wait():
    # 创建浏览器对象，自动下载安装驱动
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # 设置隐式等待时间
    driver.implicitly_wait(10)

    # 打开百度首页
    driver.get('https://www.baidu.com')

    # 在搜索框中输入关键字
    search_box = driver.find_element(by=By.NAME, value="wd")
    search_box.send_keys('Python')

    # 点击搜索按钮
    search_box.send_keys(Keys.RETURN)

    # 输出搜索结果
    results = driver.find_elements(by=By.CSS_SELECTOR, value='.result h3 a')
    for result in results:
        print(result.text)

    # 关闭浏览器
    driver.quit()


# 显式等待示例
def open_baidu_explicitly_wait():
    # 创建浏览器对象，自动下载安装驱动
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # 打开百度首页
    driver.get('https://www.baidu.com')

    # 在搜索框中输入关键字
    search_box = driver.find_element(by=By.NAME, value="wd")
    search_box.send_keys('Python')

    # 点击搜索按钮
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.result h3 a')))

    # 输出搜索结果
    results = driver.find_elements(by=By.CSS_SELECTOR, value='.result h3 a')
    for result in results:
        print(result.text)

    # 关闭浏览器
    driver.quit()


# 截图示例
def open_baidu_screenshot():
    # 创建浏览器对象，自动下载安装驱动
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # 打开百度首页
    driver.get('https://www.baidu.com')

    # 在搜索框中输入关键字
    search_box = driver.find_element(by=By.NAME, value="wd")
    search_box.send_keys('Python')

    # 点击搜索按钮
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.result h3 a')))

    # 截图，保存到当前脚本目录下
    driver.save_screenshot('baidu.png')

    # 关闭浏览器
    driver.quit()


# 对网页截长图示例
def open_baidu_screenshot_full():
    # 创建浏览器对象，自动下载安装驱动
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # 打开百度首页
    driver.get('https://www.baidu.com')

    # 在搜索框中输入关键字
    search_box = driver.find_element(by=By.NAME, value="wd")
    search_box.send_keys('Python')

    # 点击搜索按钮
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.result h3 a')))

    # 获取网页高度
    height = driver.execute_script('return document.body.scrollHeight')

    # 设置截图区域
    driver.set_window_size(1200, height)

    # 截图，保存到当前脚本目录下
    driver.save_screenshot('baidu_full.png')

    # 关闭浏览器
    driver.quit()


if __name__ == '__main__':
    open_baidu_screenshot_full()