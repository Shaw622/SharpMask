#! /usr/bin/env python3
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://go.jp.sharp/mask/")

time.sleep(3)

#名前の入力
familyName = browser.find_element_by_name('sei')
familyName.send_keys('your family name')
lastName = browser.find_element_by_name('mei')
lastName.send_keys('your last name')

#メールアドレス
eMail = browser.find_element_by_id('email')
eMail.send_keys('your email address')

#電話番号
phone = browser.find_element_by_id('tel')
phone.send_keys('your phone #')
