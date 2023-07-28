from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FindElementById():
    def locate_by_id(self):
        driver = webdriver.Chrome('C:/Users/jakub/Downloads/chromedriver_win322/chromedriver')
        driver.get('https://www.saucedemo.com/')
        login_form = driver.find_element(By.ID, 'login_credentials')
        splitted_lg = login_form.text.split()
        username = splitted_lg[3]
        username_field = driver.find_element(By.ID, 'user-name')
        username_field.send_keys(username)
        time.sleep(20)


class FindElementByClass():
    def locate_by_class(self):
        driver = webdriver.Chrome('C:/Users/jakub/Downloads/chromedriver_win322/chromedriver')
        driver.get('https://www.saucedemo.com/')
        password_form = driver.find_element(By.CLASS_NAME, "login_password")
        splitted_password = password_form.text.split()
        password = splitted_password[4]
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(password)
        time.sleep(20)



#someline
findbyid = FindElementById()
tekst = findbyid.locate_by_id()
findbyclass = FindElementByClass()
tekst2 = findbyclass.locate_by_class()




