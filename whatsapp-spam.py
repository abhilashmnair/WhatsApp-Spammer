from selenium import webdriver
driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')
victimName = input("Victim's Name : ")
spamText = input("Enter spam text : ")
driver.find_element_by_css_selector("span[title='" + victimName + "']").click()
while(True):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div[1]/div[2]').send_keys(spamText)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()