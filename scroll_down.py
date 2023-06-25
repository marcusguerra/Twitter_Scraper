from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

link = 'https://twitter.com'
scroll_delay = 4
output_file = 'output.txt'
options = Options()
options.binary_location = "C:\\Users\\cotoq\\AppData\\Local\\Mozilla Firefox\\firefox.exe"

driver = webdriver.Firefox(options=options)
driver.get(link)

a = str(input("Pronto?"))


driver.execute_script("window.open('search?q=Amazônia lang%3Apt until%3A2023-05-12 since%3A2023-01-01&src=typed_query&f=live')")

driver.close()
driver.switch_to.window(driver.window_handles[0])

time.sleep(3)

previous_height = driver.execute_script("return document.body.scrollHeight")

time.sleep(3)

while True:
    driver.execute_script("document.execCommand('selectAll'); document.execCommand('copy');")

    copied_text = driver.execute_script("return window.getSelection().toString();")

    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(copied_text + '\n')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_delay)

    if driver.execute_script("return document.body.scrollHeight") == previous_height:
        break

    previous_height = driver.execute_script("return document.body.scrollHeight")

driver.close()