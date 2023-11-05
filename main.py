import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
URL = os.environ["URL"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

#Sign in
time.sleep(1)
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
time.sleep(1)
email = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
time.sleep(1)
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
click_sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
click_sign_in.click()

#Close messages panel
time.sleep(4)
close_messages = driver.find_element(By.XPATH, '//*[@id="ember40"]')
close_messages.click()
time.sleep(1)

#Get all listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")


try:
    all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
    for listing in all_listings:
        listing.click()
        time.sleep(1)
        save = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
        save.click()
except selenium.common.exceptions.NoSuchElementException:
    driver.quit()



time.sleep(5)
driver.quit()