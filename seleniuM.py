from selenium import webdriver
import time

driver = webdriver.PhantomJS('phantomjs.exe')

def getDataIndo():
    while True:
        driver.get('https://www.covid19.go.id/')
        positipX = '/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/span[2]'
        sembuhX = '/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/span[3]'
        meninggalX = '/html[1]/body[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/span[4]'

        positif = driver.find_element_by_xpath(positipX).text
        sembuh = driver.find_element_by_xpath(sembuhX).text
        meninggal = driver.find_element_by_xpath(meninggalX).text
        join = positif+'\n'+sembuh+'\n'+meninggal
        return join
        driver.refresh()
        time.sleep(30)
        getDataIndo()

def getDataGlobal():
    while True:
        driver.get('https://ncov2019.live/')
        pathallcases = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/p[4]'
        pathdeath = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/p[6]'
        pathrecovered = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/p[10]'

        allcases = driver.find_element_by_xpath(pathallcases).text
        death = driver.find_element_by_xpath(pathdeath).text
        recovered = driver.find_element_by_xpath(pathrecovered).text

        join = 'Positif  '+allcases+'\n'+'Sembuh '+recovered+'\n'+'Meninggal '+death
        return join
        driver.refresh()
        time.sleep(30)
        getDataGlobal()

indonesia = getDataIndo()
globall = getDataGlobal()
