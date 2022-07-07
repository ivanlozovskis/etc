from time import time, sleep
from selenium import webdriver
from datetime import datetime
import telebot
import random

bot = telebot.TeleBot('5172625256:AAFiNGBCNovkjg1EeOs1XMuL-v4R2udtoXU')

PATH = r"/home/ivan/chromedriver.exe"


url = 'https://pieraksts.mfa.gov.lv/ru/moskva'



def posolstvo():
    driver = webdriver.Chrome()
    driver.get(url)

    name_path = '/html/body/main/section/form/div/div[1]/div[1]/fieldset/div[1]'

    Name = 'Иван'
    LastName = 'Шишкин'

    name = driver.find_element_by_xpath('//*[@id="Persons[0][first_name]"]')
    name.send_keys(Name)

    lname = driver.find_element_by_xpath('//*[@id="Persons[0][last_name]"]')
    lname.send_keys(LastName)

    mail = driver.find_element_by_xpath('//*[@id="e_mail"]')
    mail.send_keys('shishkinsivans@gmail.com')

    number = driver.find_element_by_xpath('//*[@id="phone"]')
    number.send_keys('+79150587838')

    submit = driver.find_element_by_xpath('//*[@id="step1-next-btn"]/button')
    submit.submit()

    arrow = driver.find_element_by_xpath('//*[@id="mfa-form2"]/div/div[1]/div/section/div/div[1]/img')
    arrow.click()

    vnj = driver.find_element_by_xpath('//*[@id="mfa-form2"]/div/div[1]/div/section/div/div[2]/div[1]/span')
    vnj.click()

    agree = driver.find_element_by_xpath(
        '//*[@id="mfa-form2"]/div/div[1]/div/section/div/div[2]/section[1]/div[2]/div[1]/span')
    agree.click()

    submit1 = driver.find_element_by_xpath(
        '//*[@id="mfa-form2"]/div/div[1]/div/section/div/div[2]/section[1]/div[2]/div[2]/button')
    submit1.click()
    next_step = driver.find_element_by_xpath('//*[@id="step2-next-btn"]/button')
    next_step.submit()

    msg = driver.find_element_by_xpath('//*[@id="mfa-form3"]/div/div[1]/div/div').text
    dates = driver.find_element_by_xpath('//*[@id="mfa-form3"]/div/div[1]/div/fieldset[1]/div/p').text
    #print(dates)
    #lst = driver.find_element_by_xpath('//*[@id="calendar-daygrid"]/tr[4]/td[6]/p').text
    #flag = False
    lll1 = {}
    l1 = []
    for i in range(5):
        for j in range(7):
            lst1 = driver.find_element_by_xpath(f'//*[@id="calendar-daygrid"]/tr[{i+1}]/td[{j+1}]/p').text
            #print(lst1)
            #driver.find_element_by_xpath(f'//*[@id="calendar-daygrid"]/tr[{i+1}]/td[{j+1}]/p').click()
            ch = list(map(int, driver.find_element_by_xpath(f'//*[@id="calendar-daygrid"]/tr[{i+1}]/td[{j+1}]/span').value_of_css_property('background-color').lstrip('rgba').replace('(', '').replace(')', '').replace('...', '').split(', ')))
            #print(ch)
            if (ch !=[0,0,0,0]) & (ch != [65, 133, 244, 1]):
                lll1[lst1] = [i,j]
                l1.append(lst1)
    #print(lll1)

    driver.find_element_by_xpath('//*[@id="calendar"]/div/div/div[2]/button[2]').click()
    sleep(3)
    time = 0
    lll = {}
    l = []
    for i in range(5):
        for j in range(7):
            lst2 = driver.find_element_by_xpath(f'//*[@id="calendar-daygrid"]/tr[{i+1}]/td[{j+1}]/p').text
            #driver.find_element_by_xpath(f'//*[@id="calendar-daygrid"]/tr[{i+1}]/td[{j+1}]/p').click()
            if list(map(int, driver.find_element_by_xpath(f'//*[@id="calendar-daygrid"]/tr[{i+1}]/td[{j+1}]/span').value_of_css_property('background-color').lstrip('rgba').replace('(', '').replace(')', '').replace('...', '').split(', '))) !=[0,0,0,0]:
                l.append(lst2)
                lll[lst2] = [i,j]
    #print(lll)
    if len(lll1) != 0:
        driver.find_element_by_xpath('//*[@id="calendar"]/div/div/div[2]/button[1]').click()
        sleep(5)
        driver.find_element_by_xpath(f'//*[@id="calendar-daygrid"]/tr[{lll1[l1[0]][0]+1}]/td[{lll1[l1[0]][1] + 1}]/p').click()
        sleep(2)
        time = driver.find_element_by_xpath('//*[@id="services"]/div[2]/div/span/select/option').text
        #print(time)
        driver.find_element_by_xpath('//*[@id="step3-next-btn"]/button').submit()
        driver.find_element_by_xpath('//*[@id="gdpr"]/span').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="mfa-form4"]/div/div[3]/button').submit()
        sleep(10)

    if len(lll) != 0:
        driver.find_element_by_xpath(f'//*[@id="calendar-daygrid"]/tr[{lll[l[0]][0] + 1}]/td[{lll[l[0]][1] + 1}]/p').click()
        sleep(2)
        time = driver.find_element_by_xpath('//*[@id="services"]/div[2]/div/span/select/option').text
        #print(time)
        driver.find_element_by_xpath('//*[@id="step3-next-btn"]/button').submit()
        driver.find_element_by_xpath('//*[@id="gdpr"]/span').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="mfa-form4"]/div/div[3]/button').submit()
        sleep(10)
    driver.quit()
    dt = [lll1, lll]
    if time != 0:
        return msg, time, dt
    return msg, 0, dt

#print(posolstvo())