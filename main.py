from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1366x768')
driver = webdriver.Chrome(service=s)

try:
    driver.get(
        "https://www.avito.ru/novorossiysk/kvartiry/sdam/na_dlitelnyy_srok/2-komnatnye-ASgBAgICA0SSA8gQ8AeQUswIkFk")
    time.sleep(1)
    while True:

        pricelist = driver.find_elements(By.XPATH,
                                         '//div [@class="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"]//span [@class="price-text-_YGDY text-text-LurtD text-size-s-BxGpL"]')
        adress = driver.find_elements(By.XPATH,
                                      '//div [@class="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"]//span [@class="geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL"]/span')
        href = driver.find_elements(By.XPATH,
                                    '//div [@class="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"]//a [@class="link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH"]')
        try:
            pricelist_xl = driver.find_elements(By.XPATH,
                                                '//div [@class="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG iva-item-xl-_jicv items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"]//span [@class="price-text-_YGDY text-text-LurtD text-size-s-BxGpL"]')
            adress_xl = driver.find_elements(By.XPATH,
                                             '//div [@class="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG iva-item-xl-_jicv items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"]//span [@class="geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL"]/span')
            href_xl = driver.find_elements(By.XPATH,
                                           '//div [@class="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG iva-item-xl-_jicv items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"]//a [@class="link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH"]')
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
            element = driver.find_element(By.XPATH,
                                          '//span [@class="pagination-item-JJq_j pagination-item_arrow-Sttbt"][@data-marker="pagination-button/next"]')
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
