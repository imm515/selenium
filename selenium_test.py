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

# 获取页面的所有文本内容
page_text = driver.find_element("tag name", "body").text

# 打印页面文本（调试用）
print(page_text)

# 将页面文本保存到 output.txt 文件中
with open("output.txt", "w") as file:
    file.write(page_text)

# 关闭浏览器
driver.quit()
