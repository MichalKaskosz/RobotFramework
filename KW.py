from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class KW():
  ROBOT_LIBRARY_SCOPE = 'GLOBAL'

  def open_site(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get('https://www.tesla.com/')
    
  def click_services(self):
    self.services = self.driver.find_element(By.XPATH, '/html/body/div[5]/main/div/div[2]/div/section/div/div/div[1]/section/a[1]')
    self.services.click()

    if self.driver.current_url == 'https://www.tesla.com/model3/design#overview' :
      print('Ponieslismy sukces! Jestesmy na:  ' + self.driver.current_url)
    else:
      print('Pyrrusowa porazka') 
