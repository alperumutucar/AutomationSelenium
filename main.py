from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='chromedriver_linux64 (1)/chromedriver')
driver.get('https://www.google.com')
text = "useinsider"

que=driver.find_element_by_xpath("//input[@name='q']")
que.send_keys(text)
que.send_keys(Keys.RETURN)

que2 = driver.find_element_by_xpath("//a[@href = 'https://useinsider.com/']")
#que2 = driver.find_element_by_xpath("//h3[@class='LC20lb DKV0Md']") both are working - this one is not unique
que2.click()

##que = driver.find_element_by_xpath("//li[@id='menu-item-5839']") takes us to the login page took so long
##que.click()

que = driver.find_element_by_xpath("//li[@id='menu-item-21643']") #to the career page
que.click()