from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import requests

def make_session():
    webdriver_service = Service(r'chrome\\chromedriver.exe')
    session = webdriver.Chrome(service=webdriver_service)
    session.set_window_size(600, 400)
    return session

def login(session):
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    loginId = config['id']['loginId']
    password = config['id']['password']

    session.get('https://secure.nnn.ed.jp/mypage/?url=%2Fhome%3F')
    try:
        WebDriverWait(session, 5).until(EC.presence_of_element_located((By.NAME, 'loginId')))
        session.find_element(By.NAME, 'loginId').send_keys(loginId)
        session.find_element(By.NAME, 'password').send_keys(password)
        session.find_element(By.CLASS_NAME, 'student-button').click()
    except:
        print('login page not found... retrying...')
        login(session)

    try:
        WebDriverWait(session, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'logout')))
    except:
        print('login failed... retrying...')
        login(session)

    print(session.page_source) #! debug

def yobiko_login(session):
    session.get('https://www.nnn.ed.nico/oauth_login?next_url=https://www.nnn.ed.nico/home&amp;target_type=n_high_school_mypage')

    print(session.page_source) #! debug

def logout(driver):
    driver.get('https://secure.nnn.ed.jp/mypage/logout')
    driver.get('https://www.nnn.ed.nico/logout')
    driver.quit()

def to_requests():
    session = make_session()
    login(session)
    yobiko_login(session)

    cookies = session.get_cookies()
    s = requests.Session()

    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])

    print(s.get('https://api.nnn.ed.nico/v1/users').text)#! debug(ログイン情報の取得)

    return s