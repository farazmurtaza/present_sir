from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import config

driver = webdriver.Chrome(
    executable_path='C:/chromedriver_win32/chromedriver.exe')
driver.get(config.facebook_group_url)

username = driver.find_element_by_id("m_login_email")
password = driver.find_element_by_id("m_login_password")
submit = driver.find_element_by_name("login")
username.send_keys(config.facebook_username)
password.send_keys(config.facebook_password)
submit.click()
time.sleep(3)

posts = driver.find_elements_by_tag_name("article")

for post in posts[0:2]:
    linesInPost = post.find_elements_by_tag_name("p")
    textArr = []
    for i in linesInPost:
        textArr.append(i.text)
    if (config.section in textArr[0]):
        # print(post.find_elements_by_tag_name("a")[3].get_attribute('href'))
        driver.get(post.find_elements_by_tag_name(
            "a")[3].get_attribute('href'))
        break
    posts = driver.find_elements_by_tag_name("article")

time.sleep(3)


textarea = driver.find_element_by_tag_name("textarea")
textarea.clear()
textarea.send_keys(config.comment)
time.sleep(3)
button = driver.find_element_by_name("submit")
time.sleep(3)
button.click()
time.sleep(2)


driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
emailInput = driver.find_elements_by_css_selector('form input')[0]
emailInput.send_keys(config.google_email)
emailInput.send_keys(Keys.ENTER)
time.sleep(5)
passwordInput = driver.find_element_by_name('password')
passwordInput.send_keys(config.google_password)
passwordInput.send_keys(Keys.ENTER)
time.sleep(5)
driver.get(config.meeting_url)
time.sleep(10)
driver.find_elements_by_xpath("//div[@role = 'button']")[3].click()
time.sleep(3)
driver.find_element_by_tag_name('body').send_keys(
    Keys.CONTROL + 'e')  # disable video
