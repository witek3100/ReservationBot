import time
from datetime import datetime
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By

def script(eml, passwd, date):
    driverB = webdriver.Chrome('\chromedriver')
    driverC = webdriver.Chrome('\chromedriver')

    driverB.get('https://panel.dsnet.agh.edu.pl/')
    driverC.get('https://panel.dsnet.agh.edu.pl/')

    email = driverB.find_element(By.ID, "username")
    email.send_keys(eml)
    email = driverC.find_element(By.ID, "username")
    email.send_keys(eml)

    password = driverB.find_element(By.ID, "password")
    password.send_keys(passwd)
    password = driverC.find_element(By.ID, "password")
    password.send_keys(passwd)

    login_button = driverB.find_element(By.CLASS_NAME, 'btn-success')
    login_button.click()
    login_button = driverC.find_element(By.CLASS_NAME, 'btn-success')
    login_button.click()

    while (1):
        res = urlopen('http://just-the-time.appspot.com/')
        result = str(res.read().strip())
        hour = result[13:18]
        if hour == '05:38':
            driverB.get('https://panel.dsnet.agh.edu.pl/reserv/rezerwuj/2193')
            rez_button = driverB.find_element(By.ID, "r_2193_2677_{}".format(date))
            rez_button.click()
            driverC.get('https://panel.dsnet.agh.edu.pl/reserv/rezerwuj/2194')
            rez_button = driverC.find_element(By.ID, "r_2194_2677_{}".format(date))
            rez_button.click()
        if result[17:20] == '0:0':
            print('{} wszystko git, czekam na 06:01...'.format(hour))
        time.sleep(1)



if __name__ == "__main__":
    email = ''
    password = ''
    date = input('rezerwowana data (RRRR-MM-DD): ')
    script(email, password, date)
