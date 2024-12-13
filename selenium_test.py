from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 配置 Chrome 的无头模式
options = Options()
options.add_argument('--headless')  # 无头模式，不打开浏览器界面
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 使用 WebDriverManager 自动下载 ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 打开 Google 网站
driver.get("https://www.google.com")

# 获取网页标题并打印
print("Page Title:", driver.title)

# 关闭浏览器
driver.quit()
