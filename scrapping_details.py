from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd

name=[]
type=[]
fare=[]
start_time=[]
end_time=[]
rating=[]
seats_left=[]
travel_time=[]
bus_link=[]
bus_route=[]

read=pd.read_csv('Andhra_buses.csv')
links=read['Route_link']
Routes=read['Route_name']

driver=webdriver.Chrome()
for link,route in zip(links,Routes):
    driver.get(link)
    time.sleep(4)
    try:
        clicks = WebDriverWait(driver,5).until(ec.presence_of_element_located((By.XPATH, "//div[@class='button']")))
        clicks.click()
    except:
        continue  
    time.sleep(3)
    old_pg=driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        new_pg=driver.execute_script("return document.body.scrollHeight")
        if new_pg==old_pg:
            break
        old_pg=new_pg
    elements=WebDriverWait(driver,35).until(ec.presence_of_all_elements_located((By.CLASS_NAME,'bus-item-details')))
    for i in elements:
            a=i.find_element(By.CLASS_NAME,'travels')
            name.append(a.text)
            b=i.find_element(By.CLASS_NAME,'bus-type')
            type.append(b.text)
            c=i.find_element(By.CLASS_NAME,"fare")
            fare.append(c.text)
            d=i.find_element(By.CLASS_NAME,'dp-time')
            start_time.append(d.text)
            e=i.find_element(By.CLASS_NAME,'bp-time')
            end_time.append(e.text)
            g=i.find_element(By.CLASS_NAME,'seat-left')
            seats_left.append(g.text)
            h=i.find_element(By.CLASS_NAME,'dur')
            travel_time.append(h.text)
            bus_link.append(link)
            bus_route.append(route)
            try:
                f=i.find_element(By.CLASS_NAME,'rating-sec')
                rating.append(f.text)
            except:
                rating.append(None)


data={"Bus_name":name,
      "Bus_type":type,
      "Bus_fare":fare,
      "start_time":start_time,
      "End_time":end_time,
      "Travel_time":travel_time,
      "Ratings":rating,
      "Seats_left":seats_left,
      "Bus_link":bus_link,
      "Bus_route":bus_route}
df = pd.DataFrame(data)
print(df)
df.to_csv('Andhra_full_1.csv')



print(*name)
print(len(name))
print(type)
print(len(type))
print(fare)
print(len(fare))
print(start_time)
print(len(start_time))
print(end_time)
print(len(end_time))
print(rating)
print(len(rating))
print(seats_left)
print(len(seats_left))
print(travel_time)
print(len(travel_time))
print(len(bus_link))