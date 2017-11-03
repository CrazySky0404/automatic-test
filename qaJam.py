import smtplib
import time
import urllib

import null as null
import selenium
import urllib3.request
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#def parse(html):
    #soup = BeautifulSoup("https://intertop.ua/personal/favorite")


def main():
    baseurl = "https://intertop.ua"
    username = "evo4ka@ua.fm"
    password = "332332"

    xpaths = {'e-mail': "//input[@name='username']",
              'Пароль': "//input[@name='password']",
              'submit': "//input[@type='submit']"
              }

    mydriver = webdriver.Chrome()
    mydriver.get(baseurl)
    mydriver.maximize_window()
    # mydriver.find_element_by_class_name('push-notification-prompt-buttons').click()

    mydriver.find_element_by_id("auth_block").click()
    time.sleep(2)
    mydriver.find_element_by_xpath(
        "//input[@name='ENTER-EMAIL'][@type='text']").send_keys(username)
    time.sleep(5)
    mydriver.find_element_by_xpath(
        "//input[@name='ENTER-PASSWORD'][@type='password']").send_keys(
        password)
    time.sleep(2)
    mydriver.find_element_by_class_name('one-log-bt').click()
    time.sleep(5)
    # mydriver.find_element_by_link_text('OUTLET %').click() # нажатие на меню
    # time.sleep(5)
    # mydriver.find_element_by_link_text('Детская обувь').click() # выбор фильтров
    # time.sleep(3)
    # mydriver.find_element_by_link_text('Гендер').click()
    # mydriver.find_element_by_link_text('Для девочек').click()
    # time.sleep(5)
    # mydriver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # прокрутка вниз страницы
    # mydriver.execute_script("window.scrollBy(0,1000)", "");
    # mydriver.find_element_by_link_text('Ecco').click()
    # time.sleep(2)
    # mydriver.find_element_by_link_text('Сапоги').click()
    # time.sleep(3)
    # mydriver.find_element_by_link_text('Показать все').click()
    # mydriver.execute_script("window.scrollBy(0,500)", "");
    # time.sleep(3)
    # mydriver.find_element_by_link_text('Ботинки').click()
    # time.sleep(4)
    # mydriver.execute_script("window.scrollBy(0,800)", "");
    # mydriver.find_element_by_link_text('Осень-зима').click()
    # time.sleep(2)
    # mydriver.execute_script("window.scrollBy(0,400)", "");
    # time.sleep(2)
    # mydriver.find_element_by_id("cat_861759").click()
    mydriver.find_element_by_xpath("//div[@class='user-menu']/div[3]").click()
    time.sleep(5)

    # mydriver.find_element_by_xpath("//*[@data-xml='3017486#3017493']").click()
    # time.sleep(2)
    # mydriver.find_element_by_link_text('В избранное').click() # добавление в избранное
    # time.sleep(10)

    proba_pera = []

    def openPage():
        for element in mydriver.find_elements_by_xpath('//div[@class = "prouct-descr-top"]'):
            print(element.text)
            mydriver.find_element_by_xpath("//div[@class='user-menu']/div[3]").click()
            time.sleep(2)



    for elem in mydriver.find_elements_by_xpath('//div[@class = "one-item-in"]'):
        #print(elem.text)
        #print("----------------------------")
        proba_pera.append(elem.text)
        #image = elem.find_element_by_tag_name("img")
        #proba_pera.append(image.get_attribute('src'))


    i = 0
    while i < len(proba_pera):
        #print(proba_pera[i])
        mydriver.find_element_by_class_name('one-item-slide-in').click()
        i += 1
        print(i)
        openPage()

        time.sleep(3)
        print(i)


#dfdf
    '''

    for elem in mydriver.find_elements_by_xpath('//div[@class = "one-item-wrap"]'):
        image = elem.find_element_by_tag_name("img")
        print(image.get_attribute('src'))
        print(elem.text )
    '''
    time.sleep(2)
    mydriver.quit();

'''
    list_name = []
    list_price = []

    for elem in mydriver.find_elements_by_xpath('//div[@class = "one-item-descr"]'):
        new_element = elem.text
        list_name.append(new_element)
    print(list_name)

    for elem in mydriver.find_elements_by_xpath('//div[@class = "one-item-price"]'):
        new_element = elem.text
        list_price.append(new_element)
    print(list_price)

    all = dict(zip(list_name, list_price))
    print(all)

'''






if __name__ == '__main__':
    main()

