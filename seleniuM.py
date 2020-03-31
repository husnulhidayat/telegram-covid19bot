from selenium import webdriver
import time

driver = webdriver.PhantomJS('phantomjs.exe')

def getDataIndo():
    while True:
        driver.get('https://www.covid19.go.id/')
        positipX = '/html/body/div[1]/div[2]/main/div/section/div/div/div[6]/div/div[1]/div/div[1]/span[3]/strong'
        sembuhX = '/html/body/div[1]/div[2]/main/div/section/div/div/div[6]/div/div[1]/div/div[1]/span[4]/strong'
        meninggalX = '/html/body/div[1]/div[2]/main/div/section/div/div/div[6]/div/div[1]/div/div[1]/span[5]/strong'

        positif = driver.find_element_by_xpath(positipX).text
        sembuh = driver.find_element_by_xpath(sembuhX).text
        meninggal = driver.find_element_by_xpath(meninggalX).text
        join = 'Positif ' +positif+'\n'+ 'Sembuh ' +sembuh+'\n'+ 'Meninggal ' +meninggal
        return join
        driver.navigate().refresh();
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
