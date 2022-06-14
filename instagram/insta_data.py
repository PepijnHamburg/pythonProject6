from selenium import webdriver
import time

path = 'driver/chromedriver.exe'
driver = webdriver.Chrome(path)

#driver.get("https://www.instagram.com/")

driver.get("https://www.instagram.com/pepain101/following/")

driver.find_element_by_xpath("/html/body/div[4]/div/div/button[2]").click()

time.sleep(5.5)

username = 'pepain101'
driver.find_element_by_name('username').send_keys(username)
password = 'Tornados12!'
driver.find_element_by_name('password').send_keys(password)

time.sleep(5.5)

driver.find_element_by_xpath\
    ("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div").click()

time.sleep(5.5)

driver.find_element_by_class_name\
    ("EforU").click()



#
# driver.get("https://www.instagram.com/pepain101/following/")

