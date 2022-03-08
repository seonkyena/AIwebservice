from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from urllib.parse import quote_plus
from urllib.request import urlopen
import time
import os


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def save_images(images, save_path):
    for index, image in enumerate(images[:1000]):  # images[:크롤링하고 싶은 사진 개수]
        src = image.get_attribute('src')
        t = urlopen(src).read()
        file = open(os.path.join(save_path, str(index + 1) + ".jpg"), "wb")
        file.write(t)
        print("img save " + save_path + str(index + 1) + ".jpg")


def make_url(name):
    # 네이버 이미지 검색
    base_url = 'https://search.naver.com/search.naver?where=image&section=image&query='
    return base_url + quote_plus(name)


def crawling_img(name):
    # URL 생성
    url = make_url(name)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager(
        chrome_type=ChromeType.CHROMIUM).install(), options=chrome_options)
    driver.implicitly_wait(3)
    driver.get(url)

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

    # 이미지 긁어오기
    images = driver.find_elements_by_class_name("_image")

    # 저장 경로 설정
    save_path = "C:\\Users\\IBK\\Documents\\kyx\\elice\\aiproject\\Naver\\" + name + "\\"
    createDirectory(save_path)

    # 이미지 저장
    save_images(images, save_path)

    # 마무리
    print(name + " 저장 성공")
    driver.close()


western_alcohol = ["탱커레이", '말리부 럼',
                   '팔리니 리몬첼로', '818 데킬라', '베일리스', '드라이 베르무트']

for i in western_alcohol:
    crawling_img(i)
