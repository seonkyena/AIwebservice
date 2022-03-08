from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.utils import ChromeType
import time
import urllib.request
import os


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def crawling_img(name):
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager(
        chrome_type=ChromeType.CHROMIUM).install(), options=chrome_options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script(
        "return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    dir = ".\google" + "\\" + name

    createDirectory(dir)  # 폴더 생성
    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute(
                "src")
            path = "C:\\Users\\IBK\\Documents\\kyx\\elice\\aiproject\\google\\" + name + "\\"
            urllib.request.urlretrieve(
                imgUrl, path + name + str(count) + ".jpg")
            count = count + 1
            if count > 1000:
                break
        except:
            pass
    driver.close()


western_alcohol = ['818 데킬라', '818 tequila']

for i in western_alcohol:
    crawling_img(i)
