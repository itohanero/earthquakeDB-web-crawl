# Author: Itohan Ero
## Adapted code from Burton Research Group

# Downloads Earthquake Permits from City Of Napa Building Department
# Site Link: https://etrakit.cityofnapa.org/etrakit/Search/permit.aspx

# need pip install selenium
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time

import csv


#Open csv file with the addresses of the buildings you want to search for
f = open('finalbuilding.csv')

addrs = [l.split(',')[0] for l in f.readlines()]

f.close()


try:

    f = open('building_address.csv')

    recorded_addr = [l.split(',')[0] for l in f.readlines()]

    f.close()

except:

    recorded_addr = []



# need chromedriver.exe installed in C:

chrome = webdriver.Chrome('insert location here')

chrome.get("https://etrakit.cityofnapa.org/etrakit/Search/permit.aspx")



for addr in addrs:

    print(addr)
    
    # page counter - makes sure all of the pages have been checked through
    check = 1

    # search twice for same addr. sometimes search doesn't go through the first time

    search_box = chrome.find_element_by_xpath('//*[@id="cplMain_txtSearchString"]')

    search_box.clear()

    search_box.send_keys(addr + '\n')

    search_box = chrome.find_element_by_xpath('//*[@id="cplMain_txtSearchString"]')

    search_box.send_keys('\n')

    time.sleep(4)

    


# find result table
# iterate through pages

    while True:

            row_count = 0
            
            try:
                time.sleep(3)
                tbody = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00"]/tbody')
            except:
                pass

            # iterate through items

            tbody = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00"]/tbody')
            
            while row_count < len(tbody.find_elements_by_tag_name('tr')):

                # get current row

                tr = tbody.find_elements_by_tag_name('tr')[row_count]

                print(tr.text)



                # if row is not for current addr, skip current row

                # cell for permit number

                td = tr.find_elements_by_tag_name('td')[0]

                # if permit number satisfies requirement
                
                
                time.sleep(3)
                
               

                if str(td.text)[:2]=='EQ':

                    permit = td.text

                    print(permit)

                    # perform double click

                    actionChains = ActionChains(chrome)

                    actionChains.double_click(td).perform()
                                                            
                    #actionChains.double_click(td).perform()




                    try:

                        # wait for permit information to show up

                                                
                        #set variables to 0 to indentify if entries aren't downlaoded correctly
                        time.sleep(3)
                        
                        type = 0
                        subtype = 0
                        description = 0
                        status = 0
                        applied = 0
                        approved = 0
                        issue = 0
                        final = 0
                        exp =  0
                        
                        # get information and write to file
                        try:
                            time.sleep(3)
                            type = str(chrome.find_element_by_xpath('//*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[1]/td[2]').text)
                        except:
                            pass

                        try:
                            #time.sleep(3)
                            subtype = str(chrome.find_element_by_xpath('//*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[2]/td[2]').text)
                        except:
                            pass
                            
                        try:
                            #time.sleep(3)
                            description = str(chrome.find_element_by_xpath('//*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[3]/td[2]').text)
                        except:
                            pass
                      
                        try:
                          #time.sleep(3)
                          status = str(chrome.find_element_by_xpath('//*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[4]/td[2]').text)
                        except:
                          pass
                          
                        try:
                            #time.sleep(3)
                            applied  = str(chrome.find_element_by_xpath('//*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[5]/td[2]').text)
                        except:
                            pass
                            
                        try:
                           # time.sleep(3)
                            approved = str(chrome.find_element_by_xpath('//*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[6]/td[2]').text)
                        except:
                            pass
                        try:
                          # time.sleep(3)
                           issue = str(chrome.find_element_by_xpath('                      //*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[7]/td[2]').text)
                        except:
                           pass
                           
                        try:
                            #time.sleep(3)
                            final = str(chrome.find_element_by_xpath('//*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[8]/td[2]').text)
                        except:
                            pass
                            
                        try:
                            #time.sleep(3)
                            exp = str(chrome.find_element_by_xpath('//*[@id="cplMain_UpdatePanelDetail"]/div[2]/table[1]/tbody/tr[9]/td[2]').text)
                        except:
                            pass
                        
                        
                
                        
    
            # Add new row to csv file with the information downloaded
                        filename = 'finalpermit.csv'
                        
                        with open(filename, 'a') as csvfile:
                            csvwriter = csv.writer(csvfile)
                            row = [addr, permit, type, subtype, description, status, applied, approved, issue, final, exp]
                            csvwriter.writerow(row)
                       

                        print(','.join([addr, permit, type, subtype, description, status, applied, approved, issue, final, exp]))


                    finally:

                        pass

                # update tbody element (otherwise will throw staleElement exception)

                tbody = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00"]/tbody')

                # update row number

                row_count += 1


            
              
            try:

                # if next page exists, go to next page
                page_num_tr = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00"]/tfoot/tr/td/table/tbody/tr[5]/td')
                
                button = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00_ctl03_ctl01_btnPageNext"]')
                
                
                if (check >= 2):
                    if '2 of 2' in page_num_tr.text:
                        print('end2')
                                           
                        prev_button = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00_ctl03_ctl01_btnPageFirst"]')
                                           
                        actionChained = ActionChains(chrome)

                        actionChained.double_click(prev_button).perform()
                                           
                        print('end2')
                                           
                        time.sleep(3)

                        break

                if(check >= 3):
                    if '3 of 3' in page_num_tr.text:
                        print('end3')
                        
                        prev_button = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00_ctl03_ctl01_btnPageFirst"]')
                                           
                        actionChained = ActionChains(chrome)

                        actionChained.double_click(prev_button).perform()
                                           
                        print('end3')
                                           
                        time.sleep(3)

                        break
                    
                if(check >= 4):
                    if '4 of 4' in page_num_tr.text:
                        print('end4')
                    
                        prev_button = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00_ctl03_ctl01_btnPageFirst"]')
                                       
                        actionChained = ActionChains(chrome)

                        actionChained.double_click(prev_button).perform()
                                       
                        print('end4')
                                       
                        time.sleep(3)

                        break
                        
                if(check >= 5):
                    if '5 of 5' in page_num_tr.text:
                        print('end5')
                    
                        prev_button = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00_ctl03_ctl01_btnPageFirst"]')
                                       
                        actionChained = ActionChains(chrome)

                        actionChained.double_click(prev_button).perform()
                                       
                        print('end5')
                                       
                        time.sleep(3)

                        break
                            
                   

               
                    
                print('else')
                    
                
                check +=1
                                        
                actionChain = ActionChains(chrome)

                actionChain.double_click(button).perform()
                    
                time.sleep(5)
                    
                    
                tbody = chrome.find_element_by_xpath('//*[@id="ctl00_cplMain_rgSearchRslts_ctl00"]/tbody')
                    

                

            except:

                break



