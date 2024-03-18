from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

def make_session():
    webdriver_service = Service(r'chrome\\chromedriver.exe')
    session = webdriver.Chrome(service=webdriver_service)
    return session

def login(session):
    config = configparser.ConfigParser()
    config.read('config.ini')

    loginId = config['id']['loginId']
    password = config['id']['password']

    session.get('https://secure.nnn.ed.jp/mypage/?url=%2Fhome%3F')
    WebDriverWait(session, 5).until(EC.presence_of_element_located((By.NAME, 'loginId')))

    session.find_element(By.NAME, 'loginId').send_keys(loginId)
    session.find_element(By.NAME, 'password').send_keys(password)
    session.find_element(By.CLASS_NAME, 'student-button').click()

    WebDriverWait(session, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'logout')))

    print(session.page_source)

def logout(driver):
    driver.quit()
