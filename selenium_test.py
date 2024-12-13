from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 配置 Chrome 的无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 启动 WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 打开目标网页
driver.get("https://example.com")

# 获取网页标题并打印
print("Page Title:", driver.title)

# 关闭浏览器
driver.quit()
