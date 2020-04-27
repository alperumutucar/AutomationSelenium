from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='chromedriver_linux64 (1)/chromedriver')
driver.get('https://www.google.com')
text = "useinsider"

assert "Google" in driver.title

que = driver.find_element_by_xpath("//input[@name='q']")
que.send_keys(text)
que.send_keys(Keys.RETURN)

#Assert.assertIn("Google", driver.title, "not google")

#assert "Google2" in driver.title  # this test fails

que2 = driver.find_element_by_xpath("//a[@href = 'https://useinsider.com/']")
# que2 = driver.find_element_by_xpath("//h3[@class='LC20lb DKV0Md']") both are working - this one is not unique
que2.click()


#assert "Google" in driver.title #should fail

assert "Insider" in driver.title

#title = driver.title
#driver.assertEqual("Useinsider", title, "webpage title error")  # checks if the title webpage is useinsider
#driver.assertNotEqual("Google", title, "The driver is still on Google")  # checks if the title of the page is not google

##que = driver.find_element_by_xpath("//li[@id='menu-item-5839']") takes us to the login page took so long
##que.click()

que = driver.find_element_by_xpath("//li[@id='menu-item-21643']")  # to the career page
que.click() #after the carreer page, I will check the teams segment in the carreer page

que = driver.find_element_by_css_selector("#career-nav > div.col.span_12.dark.center > div.vc_col-sm-1\/5.wpb_column.column_container.vc_column_container.col.centered-text.no-extra-padding.instance-5 > div > div > h4 > a")
que.click()