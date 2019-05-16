import io
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
URL = open("url.txt").read()
path = "lyric.txt"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"C:\work\chromedriver.exe", options=options)
driver.get(URL)
sleep(1)
print("ready")
lyric = driver.find_element_by_css_selector("#lyrics").text
r = open(path, "w")
r.write(lyric)
r.close()
