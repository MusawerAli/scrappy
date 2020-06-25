from selenium import webdriver
from time import sleep

class Scrappy:
    def __init__(self,keyword):
        self.driver  = webdriver.Chrome()
        # self.driver.get("https://"+website)
        self.driver.get("https://www.airbnb.com/s/"+keyword+"/homes?tab_id=all_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=search_query")
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/main/div/div/div/div[3]/aside/div/div[2]/div/button').click()
        sleep(2)
#  self.driver.find_element_by_xpath('//button[@data-testid="structured-search-input-search-button"]').click()
        # self.driver.findElement(By.data-testid("structured-search-input-search-button")).click()
        sleep(5)
        data = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/main/div/div/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div").text
        print(data)
        sleep(20)
Scrappy("dubai")