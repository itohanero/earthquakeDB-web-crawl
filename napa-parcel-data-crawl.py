# Author: Itohan Ero
## Adapted code from Burton Research Group

# Downloads Building Attributes based on Permit Number from the County of Napa Building Website
# Site Link: https://www.countyofnapa.org/150/Assessor-Parcel-Data



# need pip install selenium
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

import time

import csv



f = open('building.csv')

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

chrome.get("https://www.countyofnapa.org/150/Assessor-Parcel-Data")

for addr in addrs:

    print(addr)

    check = 1

    # search twice for same addr. sometimes search doesn't go through the first time
    time.sleep(3)

    #Switch frame since chrome.find_element_by_id would need to look at a different page
    chrome.switch_to.default_content()

    iframe = chrome.find_element_by_id('ctl00_MasterContentPlaceHolder_ContentiFrame');

    chrome.switch_to.frame(iframe)
    time.sleep(2)
    
    #Click on the clear button to clear previous entries
    clear = chrome.find_element_by_xpath('/html/body/form/p/input[2]')
    
    clear.click()
    
    time.sleep(1)
        
    form_element = chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td[3]/input')
                        
    form_element.send_keys(addr + '\n')
    
    #Make sure to switch to default frame to find the right IDs
    chrome.switch_to.default_content()

    time.sleep(2)
                    
    #click on individual assesment number
    iframe2 = chrome.find_element_by_id('ctl00_MasterContentPlaceHolder_ContentiFrame')
                    
    chrome.switch_to.frame(iframe2)
  

            
            
    try:
                permit_num = chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]')
                
                num = permit_num.text
                
                chrome.find_element_by_link_text(num).click()
    except:
                continue

    #Get Table Tbody path where the buidling attributes will be found
    try:
                time.sleep(3)
                tbody = chrome.find_element_by_xpath('/html/body/form/table/tbody')
    except:
                pass

            # iterate through items

    tbody = chrome.find_element_by_xpath('/html/body/form/table/tbody')
            
           

              




    try:

          #Set values to fix to make it easier to spot errors in the code
                        time.sleep(3)
                        
                        AssessorID = "fix"
                        TaxRate = "fix"
                        LastRecordingDate = "fix"
                        CurrentDoc = "fix"
                        PropertyType = "fix"
                        Acres = "fix"
                        LotSize = "fix"
                        AsmtDescription = "fix"
                        AsmtStatus = "fix"
                        Land = "fix"
                        StructuralImprv = "fix"
                        FixturesReal = "fix"
                        GrowingImprv = "fix"
                        TotalLand = "fix"
                        FixturesPersonal = "fix"
                        PersonalProperty = "fix"
                        ManufacturedHomes = "fix"
                        HomeownersExemption = "fix"
                        OtherExemption = "fix"
                        NetAssessedValue = "fix"
                        BuildingSeq = "fix"
                        UnitSeq = "fix"
                        BuildingCode = "fix"
                        NumberOfUnits = "fix"
                        BuildingSquare = "fix"
                        GarageSquare = "fix"
                        UnfinishedSquare = "fix"
                        YearBuilt = "fix"
                        Bedrooms = "fix"
                        FullBaths = "fix"
                        HalfBaths = "fix"
                        Fireplaces = "fix"
                        Pools = "fix"
                        
        #Gather the attributes from each row
                        AssessorID = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[7]/td[2]').text)
                        
                        TaxRate = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[8]/td[2]').text)
                        
                        LastRecordingDate = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[9]/td[2]').text)
                        
                        CurrentDoc = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[10]/td[2]').text)
                        
                        PropertyType = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[11]/td[2]').text)
                        
                        Acres = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[12]/td[2]').text)
                        
                        LotSize = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[13]/td[2]').text)
                        
                        AsmtDescription = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[14]/td[2]').text)
                        
                        AsmtStatus = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[15]/td[2]').text)
                        
                        Land = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[17]/td[2]').text)
                        
                        StructuralImprv = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[18]/td[2]').text)
                        
                        FixturesReal = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[19]/td[2]').text)
                        
                        GrowingImprv = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[20]/td[2]').text)
                        
                        TotalLand = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[21]/td[2]').text)
                        
                        FixturesPersonal = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[22]/td[2]').text)
                        
                        PersonalProperty = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[23]/td[2]').text)
                        
                        ManufacturedHomes = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[24]/td[2]').text)
                        
                        HomeownersExemption = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[25]/td[2]').text)
                        
                        OtherExemption = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[26]/td[2]').text)
                         
                        NetAssessedValue = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[27]/td[2]').text)
                          
                        BuildingSeq = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[29]/td[2]').text)
                        
                        UnitSeq = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[30]/td[2]').text)
                         
                        BuildingCode = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[31]/td[2]').text)
                          
                        NumberOfUnits = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[32]/td[2]').text)
                        
                        BuildingSquare = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[33]/td[2]').text)
                        
                        GarageSquare = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[34]/td[2]').text)
                        
                        UnfinishedSquare = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[35]/td[2]').text)
                        
                        YearBuilt = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[36]/td[2]').text)
                        
                        
                        Bedrooms = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[37]/td[2]').text)
                        
                        FullBaths = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[38]/td[2]').text)
                        
                        HalfBaths = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[39]/td[2]').text)
                        
                        Fireplaces = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[40]/td[2]').text)
                        
                        Pools = str(chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[41]/td[2]').text)
                                                  
                                                  
                                                  
                                                  
                           
                        
        #Download each of the attributes into their own row and column
                        filename = 'parcel.csv'
                        
                        with open(filename, 'a') as csvfile:
                            csvwriter = csv.writer(csvfile)
                           # row = [addr, permit, type, subtype, description, status, applied, approved, issue, final, exp]
                       
                            row = [addr
                            ,AssessorID
                            ,TaxRate
                            ,LastRecordingDate
                            ,CurrentDoc
                            ,PropertyType
                            ,Acres
                            ,LotSize
                            ,AsmtDescription
                            ,AsmtStatus
                            ,Land
                            ,StructuralImprv
                            ,FixturesReal
                            ,GrowingImprv
                            ,TotalLand
                            ,FixturesPersonal
                            ,PersonalProperty
                            ,ManufacturedHomes
                            ,HomeownersExemption
                            ,OtherExemption
                            ,NetAssessedValue
                            ,BuildingSeq
                            ,UnitSeq
                            ,BuildingCode
                            ,NumberOfUnits
                            ,BuildingSquare
                            ,GarageSquare
                            ,UnfinishedSquare
                            ,YearBuilt
                            ,Bedrooms
                            ,FullBaths
                            ,HalfBaths
                            ,Fireplaces
                            ,Pools]
                           
                            csvwriter.writerow(row)

                      

                        print(','.join([addr, AssessorID,TaxRate ,LastRecordingDate,CurrentDoc,PropertyType,Acres,LotSize,AsmtDescription,AsmtStatus,Land]))


    finally:

                    pass

               

              
    try:

    # if next page exists, go to next page
               
                print('next')

                
                new_search = chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]')
                
                chrome.find_element_by_link_text("New Search").click()
               
                    
                time.sleep(3)
                

                

    except:

                break



