from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time 

download_dir = input("please enter directory where you want to save your file: ")

user = input("Please enter your user name: ")

password = input("please enter your password: ")




# Set Firefox preferences so that the file automatically saves to disk when downloaded

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.preferences.instantApply",True)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/octet-stream, application/binary, text/csv, application/csv, application/excel, text/comma-separated-values, text/xml, application/xml")
fp.set_preference("browser.helperApps.alwaysAsk.force",False)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.folderList",0)
fp.set_preference("browser.download.dir", download_dir)

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox(firefox_profile=fp) as driver:
	driver.get("https://affiliate-program.amazon.com/")
	driver.find_element_by_id("a-autoid-0").click()
	driver.find_element_by_id("ap_email").send_keys(user)
	driver.find_element_by_id("ap_password").send_keys(password)
	driver.find_element_by_id("signInSubmit").click()
	driver.get("https://affiliate-program.amazon.com/home/reports")
	driver.find_element_by_id("ac-report-download-launcher").click()
	time.sleep(5)
	driver.find_element_by_id("ac-reports-download-generate-announce").click()
	# Wait 25 seconds so that reports gets generated and we are able to download.
	time.sleep(25)
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ac-report-download-container']/div[6]/div[3]/table/tbody/tr[1]/td[4]/a")))
	element.click()
	time.sleep(20)


	

 
