from selenium import webdriver
import time

path = 'driver/chromedriver.exe'
driver = webdriver.Chrome(path)

#driver.get("https://www.instagram.com/")

driver.get("https://www.instagram.com/pepain101/following/")

driver.find_element_by_xpath("/html/body/div[4]/div/div/button[2]").click()

time.sleep(2.5)

username = 'pepain101'
driver.find_element_by_name('username').send_keys(username)
password = 'Tornados12!'
driver.find_element_by_name('password').send_keys(password)

time.sleep(2.5)

driver.find_element_by_xpath\
    ("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div").click()

time.sleep(5.5)

driver.find_element_by_class_name\
    ("EforU").click()

time.sleep(3.5)

driver.find_element_by_xpath\
    ("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]").click()

time.sleep(2.5)

driver.find_element_by_xpath\
    ("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div")\
    .click()

time.sleep(5.5)

driver.find_element_by_class_name("_aacl _aaco _aacw _aacx _aad7 _aade")

print(test)

#
# driver.get("https://www.instagram.com/pepain101/following/")
# /html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div