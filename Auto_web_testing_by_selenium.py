from selenium import webdriver
import sys
import time

driver = webdriver.Chrome(r'D:\Python\chromedriver.exe')
driver.maximize_window()
driver.get('https://github.com/trending/python?since=monthly&spoken_language_code=en')

#signin
signIn = driver.find_element_by_css_selector('header div.d-lg-flex.flex-items-center.px-3 a.mr-3')
print(signIn)
signIn.click()
accout = driver.find_element_by_css_selector('#login_field')
pwd = driver.find_element_by_css_selector('#password')
signIn = driver.find_element_by_css_selector('input.btn.btn-primary.btn-block')
accountStr = input("----------\nEnter your account:\n----------\n")
pwdStr = input("----------\nEnter your pwd: \n----------\n")
# accountStr='whylovechina@gmail.com'
# pwdStr='why**********@'
accout.send_keys(accountStr)
pwd.send_keys(pwdStr)
signIn.click()

# this page has been jumped to two-factor page
authentic = driver.find_element_by_css_selector('#otp') # select input
authenticationStr = input("----------\nEnter your Authentication code:\n----------\n")
authentic.send_keys(authenticationStr)
verify = driver.find_element_by_css_selector('button.btn.btn-primary.btn-block')
verify.click()
# select all the project
i = 0

# for pj in driver.find_elements_by_css_selector('article.Box-row h1 a'):
#     if i>=10:
#         break
#     i+=1
#     driver.execute_script("window.open();")
#     handles = driver.window_handles
#     url = pj.get_attribute("href")
#     driver.switch_to.window(handles[1])
#     driver.get(url)
#     time.sleep(10)
#     driver.close()
    
# selenium.common.exceptions.StaleElementReferenceException: 
#   Message: stale element reference: element is not attached to the 
# page document    
while (i<10):
    pj = driver.find_elements_by_css_selector('article.Box-row h1 a')[i]
    pj.click()
    watch = driver.find_element_by_css_selector('summary.btn.btn-sm.btn-with-count')
    choices = driver.find_elements_by_css_selector('button[type = submit][name = do]')
    watch.click()
    choices[0].click()
    time.sleep(2)
    watch.click()
    choices[1].click()
    time.sleep(10)
    driver.back()
    i=i+1
pass 