from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import constants

s = Service(ChromeDriverManager().install())  # это установка драйвера
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1366x768')
driver = webdriver.Chrome(service=s)

try:
    driver.get(constants.URL) # ссылка на сайт который парсим
    time.sleep(1)
    while True:

        pricelist = driver.find_elements(By.XPATH, constants.pricelist)
        adress = driver.find_elements(By.XPATH, constants.adress)
        href = driver.find_elements(By.XPATH, constants.href)

        try:
            pricelist_xl = driver.find_elements(By.XPATH, constants.pricelist_xl)
            adress_xl = driver.find_elements(By.XPATH, constants.adress_xl)
            href_xl = driver.find_elements(By.XPATH, constants.href_xl)

            pricelist += pricelist_xl
            adress += adress_xl
            href += href_xl
        except:
            pass
        print(len(pricelist))
        for i in range(len(pricelist)):
            print(adress[i].text, pricelist[i].text, href[i].get_attribute('href'))
        time.sleep(1)
        try:
            action = ActionChains(driver)
            element = driver.find_element(By.XPATH, constants.NEXTBUTTON)
            action.move_to_element(element).perform()
            element.click()
            print(driver.current_url)
            time.sleep(10)
        except:
            break
    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
