from selenium import webdriver

# 打开chrome 后获取网页源码 最后关闭
# browser = webdriver.Chrome()
#
# browser.get('http://www.baidu.com')
# print(browser.page_source)
# browser.close()

# from selenium.webdriver.common.by import By
# brower = webdriver.Chrome()
#
# brower.get("http://www.taobao.com")
# 元素查找
# input_first = brower.find_element(By.ID,"q")
# print(input_first)

# 多元素查找
# lis = brower.find_elements(By.CSS_SELECTOR,".service-bd li")
# print(lis)

# brower.close()

# 元素交互
# import time
# from selenium.webdriver.common.by import By
#
# brower = webdriver.Chrome()
# brower.get("http://www.taobao.com")
#
# input_str = brower.find_element(By.ID,"q")
# input_str.send_keys("ipad")
#
# time.sleep(1)
# input_str.clear()
#
# input_str.send_keys("huawei")
# button = brower.find_element(By.CLASS_NAME,"btn-search")
# button.click()

# 获取元素属性
# from selenium.webdriver.common.by import By
# brower = webdriver.Chrome()
#
# url = 'https://www.zhihu.com/explore'
# brower.get(url)
#
# logo = brower.find_element(By.ID,"zh-top-link-logo")
# print(logo)
# print(logo.get_attribute('class'))
