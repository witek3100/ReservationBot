import time
from urllib.request import urlopen
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def script(eml, passwd, date):
    while (1):
        res = urlopen('http://just-the-time.appspot.com/')
        result = str(res.read().strip())
        hour = result[13:18]
        if hour == "03:56":
            driver = webdriver.Chrome('\chromedriver')
            driver.get('https://panel.dsnet.agh.edu.pl/')
            email = driver.find_element(By.ID, "username")
            email.send_keys(eml)
            password = driver.find_element(By.ID, "password")
            password.send_keys(passwd)
            login_button = driver.find_element(By.CLASS_NAME, 'btn-success')
            login_button.click()
            while (1):
                res = urlopen('http://just-the-time.appspot.com/')
                result = str(res.read().strip())
                hour = result[13:18]
                if hour:
                    driver.get('https://panel.dsnet.agh.edu.pl/reserv/rezerwujGrupe/2192')
                    buttons_ids = [2677, 2676]
                    for button_id in buttons_ids:
                        try:
                            buttonB = driver.find_element(By.ID, "r_2193_{}_{}".format(button_id, date))
                            buttonC = driver.find_element(By.ID, "r_2194_{}_{}".format(button_id, date))
                        except selenium.common.exceptions.NoSuchElementException:
                            continue
                        else:
                            buttonB.click()
                            buttonC.click()
                            print('zarezerwowane cale boisko')
                            return 0
                    for button_id in buttons_ids:
                        try:
                            buttonB = driver.find_element(By.ID, "r_2193_{}_{}".format(button_id, date))
                        except selenium.common.exceptions.NoSuchElementException:
                            pass
                        else:
                            buttonB.click()
                            print('zarezerwowana polowka')
                            return 0
                        try:
                            buttonC = driver.find_element(By.ID, "r_2193_{}_{}".format(button_id, date))
                        except selenium.common.exceptions.NoSuchElementException:
                            pass
                        else:
                            buttonC.click()
                            print('zarezerwowana polowka')
                            return 0
                    print('nie udalo sie zarezerwowac')
                    return 1

        if result[17:20] == '0:0':
            print('{} wszystko git, czekam na 06:01...'.format(hour))
        time.sleep(1)

if __name__ == "__main__":
    email = 'nowogorski@student.agh.edu.pl'
    password = 'nihospif8F'
    date = input('rezerwowana data (RRRR-MM-DD): ')
    script(email, password, date)
