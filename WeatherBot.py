from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver

def getWeather():
    Date = datetime.today().strftime('%Y-%m-%d')
    URL = "https://www.metoffice.gov.uk/weather/forecast/gcqg3t9ej#?date=" + str(Date)
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get(URL)
    sleep(1)
    decline_cookies = browser.find_element(By.CLASS_NAME,"ccc-notify-button.ccc-tabbable.ccc-accept-button")
    decline_cookies.click()
    sleep(1)
    high_temp = browser.find_element(By.CLASS_NAME,"tab-temp-high").text
    low_temp = browser.find_element(By.CLASS_NAME,"tab-temp-low").text
    desc = browser.find_element(By.ID,"tabSummaryText2023-07-12").text
    browser.close()
    return high_temp, low_temp, desc

high_temp, low_temp, desc = getWeather()
Date = datetime.today().strftime('%d/%m/%Y')
print("The weather for",str(Date)+":"
      "\n"+str(desc),
      "\nHigh Temperature:",high_temp,
      "\nLow Temperature:",low_temp)
