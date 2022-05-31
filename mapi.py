from selenium import webdriver
driver = webdriver.Chrome() 
driver.get("http://www.google.com")
for elem in driver.find_elements_by_xpath('.//span[@class = "gbts"]'):
    print(elem.text)
