
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


#-------------------------------------- USER INPUTS -------------------------------------

MOBILE_NUMBER = XXXXXXXXXX
PIN_CODES = [411044 , 411035 , 411027 ]				# Seperate PIN CODES with comma
WEBDRIVER_PATH = r""
OTP_SLEEP_TIME =  25					# Optional
MEMBERS_SLEEP_TIME =  10				# Optional


#------------------------------------- VARIABLES & DRIVER ---------------------------------

URL = "https://selfregistration.cowin.gov.in/"

driver = webdriver.Chrome(executable_path = WEBDRIVER_PATH) # FOR CHROME
#driver = webdriver.Firefox(executable_path = WEBDRIVER_PATH) # FOR FIREFOX

driver.get(URL)
 


#-------------------------------------- HANDLES LOGIN PROCESS --------------------------------

def register(number):
	driver.find_element_by_xpath("//input[@id='mat-input-0']").send_keys(number)
	driver.find_element_by_xpath("//ion-button[contains(text(),'Get OTP')]").click()

	# ------------ WAITS FOR USER TO ENTER OTP
	time.sleep(OTP_SLEEP_TIME)
	driver.find_element_by_xpath("//ion-button[contains(text(),'Verify & Proceed')]").click()

	# ------------ WAITS FOR USER TO SELECT CANDIDATES
	time.sleep(MEMBERS_SLEEP_TIME)
	driver.find_element_by_xpath("//ion-button[contains(text(),'Schedule Now')]").click()


#----------------------------------- SEARCHES FOR PIN_CODE -------------------------------------

def search_pin(pin):
	time.sleep(2)
	driver.find_element_by_xpath("//input[@id='mat-input-2']").send_keys(pin)
	driver.find_element_by_xpath("//ion-button[contains(text(),'Search')]").click()
	driver.find_element_by_xpath("//input[@id='mat-input-2']").clear()


	#--------------- Below line filters by selecting AGE18+ button
	driver.find_element_by_xpath("//label[@for='c1']").click()


def scrap_loop():

	links = driver.find_elements_by_css_selector("ion-row.hydrated li.ng-star-inserted div.vaccine-box a")

	for i in links:
		status = i.get_attribute("innerHTML")
		if status != ' Booked ' and status != ' NA ': 
			i.click()
			return True

	return False

# ---------------------- MAIN ---------------------


register(MOBILE_NUMBER)

while True:

	r = random.randint(0,len(PIN_CODES)-1)
	search_pin(PIN_CODES[r])
	available = scrap_loop()
	if available:
		break



