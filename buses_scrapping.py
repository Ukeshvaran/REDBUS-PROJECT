from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import time
#Andhra
def Andhra():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,6):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    Apsrtc_buses=({"Route_name":route_name,"Route_link":route_link})
    df_1=pd.DataFrame(Apsrtc_buses)

    df_1.to_csv('Andhra_buses.csv')
    driver.close()

#kerala
def kerala():
        route_name=[]
        route_link=[]


        driver=webdriver.Chrome()
        driver.get('https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile')
        wait=WebDriverWait(driver,25)
        driver.maximize_window()
        time.sleep(3)

        for j in range(1,3):
            routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
            for i in routes:
                route_name.append(i.text)
                link=i.get_attribute("href")
                route_link.append(link)
            try:
                page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
                next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
                time.sleep(2)
                driver.execute_script("arguments[0].click();",next_page)
                time.sleep(3)
            except:
                break

        ksrtc_buses=({"Route_name":route_name,"Route_link":route_link})
        df_2=pd.DataFrame(ksrtc_buses)

        df_2.to_csv('Kerala_buses.csv')
        driver.close()

#Telengana
def telengana():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,4):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    tsrtc_buses=({"Route_name":route_name,"Route_link":route_link})
    df_3=pd.DataFrame(tsrtc_buses)

    df_3.to_csv('telengana_buses.csv')
    driver.close()

#punjab
def punjab():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/pepsu/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,3):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    punjab_buses=({"Route_name":route_name,"Route_link":route_link})
    df_4=pd.DataFrame(punjab_buses)

    df_4.to_csv('punjab_buses.csv')
    driver.close()

#Rajasthan
def Rajasthan():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,3):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    Rsrtc_buses=({"Route_name":route_name,"Route_link":route_link})
    df_5=pd.DataFrame(Rsrtc_buses)

    df_5.to_csv('Rajasthan_buses.csv')
    driver.close()

#South_bengal
def south_bengal():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,6):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    sb_buses=({"Route_name":route_name,"Route_link":route_link})
    df_6=pd.DataFrame(sb_buses)

    df_6.to_csv('South_bengal_buses.csv')
    driver.close()

#Himachal
def himachal():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,5):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    hrtc_buses=({"Route_name":route_name,"Route_link":route_link})
    df_7=pd.DataFrame(hrtc_buses)

    df_7.to_csv('himachal_buses.csv')
    driver.close()

#assam
def assam():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/astc/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,6):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    astc_buses=({"Route_name":route_name,"Route_link":route_link})
    df_8=pd.DataFrame(astc_buses)

    df_8.to_csv('assam_buses.csv')
    driver.close()

#up
def up():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,6):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    up_buses=({"Route_name":route_name,"Route_link":route_link})
    df_9=pd.DataFrame(up_buses)

    df_9.to_csv('up_buses.csv')
    driver.close()

#west_bengal
def west_bengal():
    route_name=[]
    route_link=[]


    driver=webdriver.Chrome()
    driver.get('https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile')
    wait=WebDriverWait(driver,25)
    driver.maximize_window()
    time.sleep(3)

    for j in range(1,5):
        routes=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="route"]')))
        for i in routes:
            route_name.append(i.text)
            link=i.get_attribute("href")
            route_link.append(link)
        try:
            page=wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="DC_117_paginationTable"]')))
            next_page=page.find_element(By.XPATH,f'//div[@class="DC_117_pageTabs " and text()={j+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].click();",next_page)
            time.sleep(3)
        except:
            break

    wbtc_buses=({"Route_name":route_name,"Route_link":route_link})
    df_10=pd.DataFrame(wbtc_buses)

    df_10.to_csv('west_bengal_buses.csv')
    driver.close()

Andhra()
time.sleep(10)
kerala()
time.sleep(10)
telengana()
time.sleep(10)
punjab()
time.sleep(10)
Rajasthan()
time.sleep(10)
south_bengal()
time.sleep(10)
himachal()
time.sleep(10)
assam()
time.sleep(10)
up()
time.sleep(10)
west_bengal()


