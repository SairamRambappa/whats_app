from selenium import webdriver
from selenium.common.exceptions import *
import time
import sys
from datetime import datetime,date
import csv
#staging


driver = webdriver.Chrome(r"chromedriver")
driver.get('https://web.whatsapp.com')

input('Enter anything after scanning QR code')
time.sleep(5)
name = input('Enter the name of user or group : ')


user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

time.sleep(5)
def check_exists_by_xpath():
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span').text == "online"
    except NoSuchElementException as ex:
        return 0,"offline"
    return 1,"online"


interval_min = sys.argv[1]
duration = sys.argv[2]
#Converting interval_min to seconds for time.sleep()
sleep_param = int(interval_min) * 60
#Calculation the counter 
counter_param = int((int(duration) * 3600 ) / sleep_param)


counter = 1

with open("status_timesheet.csv","w+",newline='') as csvfile:
	fieldnames = ['name', 'time', 'status']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	while True:
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		writer.writerow({'name':name, 'time':dt_string,'status': check_exists_by_xpath()[1]})
		time.sleep(sleep_param)
		counter += 1
		if counter == counter_param:
			break

