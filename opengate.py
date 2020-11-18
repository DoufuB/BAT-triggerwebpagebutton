from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://192.168.1.3")
button = driver.find_element_by_id('opb')
button.click()

driver.close()
driver.quit()