from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get("https://www.instagram.com/explore/tags/<tag>/")

decline_cookies = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
decline_cookies.click()

sleep(1)

log_in = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div[2]/div[1]/a")
log_in.click()

sleep(1)

username_input = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
password_input = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
username_input.send_keys("<name>")
password_input.send_keys("<password>")

sleep(1)

log_in = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]")
log_in.click()

sleep(1)

not_now = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
not_now.click()

sleep(1)
post = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main")
post.click()

sleep(1)

for i in range(2):
    next_post = browser.find_element(By.CLASS_NAME,"_abl-")
    next_post.click()

    sleep(1)
    
    like_post = browser.find_element(By.CLASS_NAME,"_aamw")
    like_post.click()
    
    #comment_input = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/section/div/form/div/textarea")
    #comment_input.send_keys("<comment>")
    #send_comment = browser.find_element(By.CLASS_NAME," _am-5")
    #send_comment.click()
    
sleep(5)
browser.close()
