from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
options=Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.bt.com/")
driver.maximize_window()
time.sleep(7)

mouse=ActionChains(driver)
cookie=driver.find_elements(By.CSS_SELECTOR,"a.call")
if cookie==True:
    mouse.click()
#mouse.move_to_element(cookie).click()
time.sleep(3)

mouse=ActionChains(driver)
mobile=driver.find_element(By.XPATH,"//*[@id='bt-navbar']/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/a/span")
mouse.move_to_element(mobile).perform()

mouse=ActionChains(driver)
cookie=driver.find_elements(By.CSS_SELECTOR,"a.call")
if cookie==True:
    mouse.click()
time.sleep(3)

driver.get("https://www.bt.com/products/mobile/phones/")
mouse=ActionChains(driver)
cookie=driver.find_elements(By.CSS_SELECTOR,"a.call")
if cookie==True:
    mouse.click()


time.sleep(7)
mouse=ActionChains(driver)
down=driver.find_element(By.LINK_TEXT,"View SIM only deals")
mouse.scroll_to_element(down).perform()
time.sleep(2)


driver.find_element(By.XPATH,"//body").send_keys(Keys.CONTROL + 't')
driver.get("https://www.bt.com/products/mobile/sim-only-deals/")
mouse=ActionChains(driver)
cookie=driver.find_elements(By.CSS_SELECTOR,"a.call")
if cookie==True:
    mouse.click()
time.sleep(3)
data=driver.find_element(By.XPATH,"//*[@id='__next']/div/div[4]/div[2]/div/div[2]/div[10]/div[1]")
text="30% off and double data"
if text in data.text:
    print("True")
driver.quit()