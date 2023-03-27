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
        if hour == '12:46':
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
                if hour == '12:47':
                    driver.get('https://panel.dsnet.agh.edu.pl/reserv/rezerwujGrupe/2192')
                    buttons_ids_dict = {2677:'22:30', 2676:'21:00', 2675:'19:30', 2674:'18:00', 2673:'16:30',
                                        2137:'22:30', 2136:'21:00', 2135:'19:30', 2134:'18:00', 2133:'16:30'}
                    for button_id in buttons_ids_dict.keys():
                        try:
                            buttonB = driver.find_element(By.ID, "r_2193_{}_{}".format(button_id, date))
                            buttonC = driver.find_element(By.ID, "r_2194_{}_{}".format(button_id, date))
                        except selenium.common.exceptions.NoSuchElementException:
                            print('cale boisko: {} zajete'.format(buttons_ids_dict[button_id]))
                            continue
                        else:
                            buttonB.click()
                            buttonC.click()
                            print('ZAREZERWOWANE CALE {}'.format(buttons_ids_dict[button_id]))
                            return 0
                    for button_id in buttons_ids_dict.keys():
                        try:
                            buttonB = driver.find_element(By.ID, "r_2193_{}_{}".format(button_id, date))
                        except selenium.common.exceptions.NoSuchElementException:
                            print('polowka B: {} zajete'.format(buttons_ids_dict[button_id]))
                        else:
                            buttonB.click()
                            print('ZAREZERWOWANA POLOWKA {}'.format(buttons_ids_dict[button_id]))
                            return 0
                        try:
                            buttonC = driver.find_element(By.ID, "r_2193_{}_{}".format(button_id, date))
                        except selenium.common.exceptions.NoSuchElementException:
                            print('polowka C: {} zajete'.format(buttons_ids_dict[button_id]))
                        else:
                            buttonC.click()
                            print('ZAREZERWOWANA POLOWKA {}'.format(buttons_ids_dict[button_id]))
                            return 0
                    print('nie udalo sie zarezerwowac')
                    return 1

        if result[17:20] == '0:0':
            print('{} - oczekiwanie na otwarcie rezerwacji...'.format(hour))
        time.sleep(1)

if __name__ == "__main__":
    email = 'nowogorski@student.agh.edu.pl'
    password = 'nihospif8F'
    date = input('rezerwowana data (RRRR-MM-DD): ')
    script(email, password, date)
