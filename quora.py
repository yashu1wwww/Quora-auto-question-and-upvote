from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://www.quora.com/?time=1690983559898915&uid=449470134&unh=ff66459ec1f9a2ad7b10a9a2a796023c")

# Log in to Quora
driver.find_element_by_name("email").send_keys("quora1675@gmail.com") #replace with your gmail
time.sleep(3)
driver.find_element_by_name("password").send_keys("quora11@#") #replace with your password
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button/div/div/div').click() #login button
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]').click() #what do you want ask or share?
time.sleep(3)

#ask a question....
driver.find_element_by_css_selector("#root > div > div:nth-child(2) > div > div > div > div > div.q-flex.ModalContainerInternal___StyledFlex-s8es4q-2.modal_content_inner.qu-flexDirection--column.qu-bg--white.qu-overflowY--auto.qu-borderAll.qu-alignSelf--center > div > div > div.q-flex.qu-flexDirection--column.qu-overflowY--auto > div.q-relative.qu-display--flex.qu-flexDirection--column > div > div.q-box > div > div > div > div > div.q-box.qu-pt--small > div > div > div.q-flex.qu-alignItems--center.qu-bg--white.qu-borderColor--gray.qu-hover--borderColor--blue.qu-hover--zIndex--1.qu-borderBottom.qu-pb--small.InputStyleWrapper___StyledFlex-sc-1d0740s-0 > div > div > textarea").send_keys("nothing mobile found on road") #question feed 
time.sleep(4)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/button[2]/div/div/div').click() #add question submit button
time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div/div/button/div/div/div').click() #add original question
time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/button').click() #done

#post it...
#driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/div/div[2]/div/div[1]/div').click() #click on post button
#time.sleep(3)
#driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div').send_keys("my first tweet") #text in question button
#time.sleep(3)
#driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]').click() #post button click

#Upvote,downvote & add the comment 
driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/button/div[2]/div/span/span[2]/span').click() #upvote button click
time.sleep(4)
#driver.find_element_by_css_selector("#mainContent > div > div > div:nth-child(2) > div > div > div > div > div > div > div > div:nth-child(1) > div.q-box > div > div > div > div.q-box.qu-zIndex--action_bar > div > div > div:nth-child(1) > div:nth-child(1) > div > div > div > div.q-box.qu-display--inline-block > div > button > div > span > span > svg").click() #downvote button click(if you want)
#time.sleep(4)
driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div').click() #comment button click
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div/div/div[1]/div').send_keys('best one') #add a comment
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mainContent"]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div').click() #comment button click
time.sleep(7)
driver.close()
