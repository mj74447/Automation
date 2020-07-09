from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://apps.who.int/trialsearch')
searchbox = driver.find_element_by_xpath('//*[@id="TextBox1"]')
searchbox.send_keys('lupus')
searchButton = driver.find_element_by_xpath('//*[@id="Button1"]')
searchButton.click()

button2 = driver.find_element_by_xpath('//*[@id="Button7"]')
button2.click()
