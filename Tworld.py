#!/usr/local/bin/python3.6
from selenium import webdriver
import time
import sys
import os
import platform

class Tworld():
    driver = ""
    user_id = ""
    user_pass = ""

    def __init__(self):
        if platform.system() == "Darwin": # OSX
            options = webdriver.ChromeOptions()
            #options.add_argument('headless')
            options.add_argument("lang=ko_KR")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

            self.driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        else:
            self.driver = webdriver.PhantomJS()

        self.driver.implicitly_wait(3)

    def login(self, user_id, user_pass):
        try:
            self.user_id = user_id
            self.user_pass = user_pass

            self.driver.get('http://www.tworld.co.kr/poc/html/main/MA.html')

            self.driver.switch_to.frame('login_area')
            self.driver.find_element_by_xpath('//*[@id="authLogin"]').click()
            self.driver.switch_to.window('loginPop')
            self.driver.find_element_by_id('userId').send_keys(self.user_id)
            self.driver.find_element_by_id('password').send_keys(self.user_pass)
            self.driver.find_element_by_id('authLogin').click()
            time.sleep(1)
            return True

        except:
            return False

    def get_available_data_in_mb(self):
        self.driver.switch_to.window('')
        self.driver.switch_to.frame('login_area')
        self.driver.switch_to.frame('freebillIframe')
        data = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/span[1]').text
        value, standard = data.split(" ")
        self.driver.quit()

        if standard == "MB":
            data = value.replace(",", "")
        elif standard == "GB":
            data = float(value) * 1000
        else:
            data = "999"
        return data


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("arguments required.")
        exit(0)

    user_id = sys.argv[1]
    user_pass = sys.argv[2]

    tworld = Tworld()
    if tworld.login(user_id, user_pass):
        print(tworld.get_available_data_in_mb())