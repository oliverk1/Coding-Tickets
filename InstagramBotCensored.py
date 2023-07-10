from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

comments = ["comment1","comment2"]

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get("https://www.instagram.com/explore/tags/<tag>/")

decline_cookies = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
decline_cookies.click()

sleep(2)

log_in = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div/div[2]/div[1]/a")
log_in.click()

sleep(2)

username_input = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
password_input = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
username_input.send_keys("<username>")
password_input.send_keys("<password>")

sleep(2)

log_in = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]")
log_in.click()

sleep(2)

not_now = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
not_now.click()

sleep(2)

post = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main")
post.click()

sleep(2)

for i in range(15):
    comment = random.choice(comments)
    
    next_post = browser.find_element(By.CLASS_NAME,"_aaqg._aaqh")
    next_post.click()

    sleep(2)
    
    like_post = browser.find_element(By.CLASS_NAME,"_aamw")
    like_post.click()
    
    comment_input = browser.find_element(By.CLASS_NAME,"x1i0vuye.xvbhtw8.x76ihet.xwmqs3e.x112ta8.xxxdfa6.x5n08af.x78zum5.x1iyjqo2.x1qlqyl8.x1d6elog.xlk1fp6.x1a2a7pz.xexx8yu.x4uap5.x18d9i69.xkhd6sd.xtt52l0.xnalus7.xs3hnx8.x1bq4at4.xaqnwrm")
    comment_input.send_keys(comment)
    send_comment = browser.find_element(By.CLASS_NAME,"_am-5")
    send_comment.click()
    
sleep(5)
browser.close()
