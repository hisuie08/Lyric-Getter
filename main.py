import io
import re
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
if re.compile("kasi-time.com").search(URL):
    lyric = driver.find_element_by_css_selector("#lyrics").text
elif re.compile("uta-net.com").search(URL):
    lyric = driver.find_element_by_css_selector("#kashi_area").text
elif re.compile("utaten.com").search(URL):
    lyric = driver.find_element_by_css_selector("#contents > main > article > div.lyricBody > div > div.hiragana").text
elif re.compile("j-lyric.net").search(URL):
    lyric = driver.find_element_by_css_selector("#Lyric").text
r = open(path, "w")
r.write(lyric)
r.close()
