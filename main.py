from selenium import webdriver
from time import sleep

class Scrappy:
    def __init__(self,website):
        self.driver  = webdriver.Chrome()
        self.driver.get("https://"+website)
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[1]/div[1]/div/div/label').send_keys('dubai')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div/div/form/div/div[2]/button/span[1]/span').click()

        sleep(10)
Scrappy("airbnb.com")