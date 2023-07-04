from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def writeHtml(html_content):
    file_path = "agro.html"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

def run(palavraChave):
    link = 'https://chrome.google.com/webstore/detail/old-twitter-layout-2023/jgejdcdoeeabklepnkdbglgccjpdgpmf'
    scroll_delay = 5
    output_file = 'output.txt'
    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    service = Service("C:\\Users\\cotoq\\OneDrive\\Área de Trabalho\\tp_ftc\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(link)
    a = str(input("Pronto?"))
    driver.switch_to.window(driver.window_handles[0])

    try:
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_delay)
            writeHtml(driver.page_source)
    except KeyboardInterrupt:
        driver.quit()








palavraChave = "mst"
run(palavraChave)

