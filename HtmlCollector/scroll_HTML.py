from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pickle
import time

def writeHtml(html_content):
    file_path = "agro.html"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)



def run(palavraChave):
    link = 'https://twitter.com'
    scroll_delay = 4
    output_file = 'output.txt'
    options = Options()
    options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

    driver = webdriver.Firefox(options=options)
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

