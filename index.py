from selenium import webdriver
from selenium.webdriver.common import keys
import time

# 變更預設下載路徑
filePath = r'/Users/####/Downloads/####'
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": filePath,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

browser = webdriver.Chrome(chrome_options=options)

loginUrl = 'target login url'
userName = ('####')
password = ('####')

# 登入
browser.get(loginUrl)
browser.find_element_by_css_selector('input[name="loginname"]').send_keys(userName)
browser.find_element_by_css_selector('input[name="pwd"]').send_keys(password)
browser.find_element_by_css_selector('input[value="登入"]').send_keys(keys.Keys.ENTER)
# mac 鍵盤指令新開分頁
body = browser.find_element_by_tag_name('body').send_keys(keys.Keys.COMMAND + 't')

targetUrl = 'target download url'
browser.get(targetUrl)
# 跳轉到新開分頁
browser.find_element_by_tag_name('body').send_keys(keys.Keys.COMMAND + keys.Keys.PAGE_UP)
date = '2017/01/26'
browser.find_element_by_css_selector('input[name="DD"]').clear()
browser.find_element_by_css_selector('input[name="DD"]').send_keys(date)
browser.find_element_by_css_selector('input[value="CSV下載"]').send_keys(keys.Keys.ENTER)
# 預留等待時間，避免下載結束前關閉瀏覽器造成副檔名錯誤
time.sleep(60)
browser.quit()

