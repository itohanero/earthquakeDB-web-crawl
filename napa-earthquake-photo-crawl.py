# Author: Itohan Ero
## Adapted code from Burton Research Group

# Downloads images from NAPA Earthquake Photo Gallery
# Site Link: http://learningfromearthquakes.org/2014-08-24-south-napa/photo-gallery

# need pip install selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# need chromedriver.exe installed in C:
chrome = webdriver.Chrome('insert location here')
chrome.get("http://learningfromearthquakes.org/2014-08-24-south-napa/photo-gallery")


#continues until there are no more images left
try:
    exist = WebDriverWait(chrome, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="original_filename_image"]'))
    )
    
    ID = chrome.find_element_by_xpath('//*[@id="attachment_id_r"]').text

    while True:

        ID = chrome.find_element_by_xpath('//*[@id="attachment_id_r"]').text
        print ('%s\n'%(ID))
        
        download_btn = chrome.find_element_by_xpath('//*[@id="original_filename_anchor"]')
        download_btn.click()
        time.sleep(5)

        next_btn = chrome.find_element_by_xpath('//*[@id="sp-component"]/div/div[4]/div/div[2]/div/div[1]/div[2]/a/strong')
        next_btn.click()
        time.sleep(1)

        try:
            exist = WebDriverWait(chrome, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="original_filename_image"]'))
            )
        except Exception as e:
            raise e


        

except Exception as e:
    raise e



chrome.close()

