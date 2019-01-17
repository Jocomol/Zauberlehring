from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()
driver.get("https://littlealchemy2.com/")
time.sleep(2)
play = driver.find_element_by_class_name("loading-screen-container")
play.click()
print ("start")
#time.sleep(1)
#settings = driver.find_element_by_xpath("/hmtl/body/div[1]/div[2]/div[4]/div[2]/div[2]")

def isnewelement(newelementcontainer):
    library = driver.find_element_by_id("library")
    elementsnamechecklist = library.find_elements_by_class_name("element")
    already = False
    try:
        for elementsnamecheck in elementsnamechecklist:
            elemnamecheckname = elementsnamecheck.find_element_by_class_name("elementName")
            name_to_check = newelementcontainer.find_element_by_tag_name("img").get_attribute("alt")
            already = str(name_to_check) == str(elemnamecheckname.text) ##Doesn't Work
        return already
    except NoSuchElementException:
        return False
    return True

def clearworkspace():
    settings.click()
    time.sleep(1)
    cleanup = driver.find_element_by_xpath("//*[contains(text(), 'clean up')]")
    cleanup[0].click()
    time.sleep(1)

def findelements():
    library = driver.find_element_by_id("library")
    elements = library.find_elements_by_class_name("element")
    for elem in elements:
        elemname = elem.find_element_by_class_name("elementName")
        elempic = elem.find_element_by_tag_name("img")
        for elem2 in elements:
            elempic2 = elem2.find_element_by_tag_name("img")
            elemname2 = elem.find_element_by_class_name("elementName")
            workspace = driver.find_element_by_id('workspace')
            ActionChains(driver).drag_and_drop(elempic, workspace).perform()
            print ("Element 1 dragged")
            ActionChains(driver).drag_and_drop(elempic2, workspace).perform()
            print ("Element 2 dragged")
            time.sleep(2)
            newelementcontainer = driver.find_element_by_class_name("new-element-image-container")
            if isnewelement(newelementcontainer):
                print ("new element")
                newelementname = newelementcontainer.find_element_by_tag_name("img").get_attribute("alt")
                #print (elemname + "+" + elemname2 + "=" + newelementname + ".")
                newelementcontainer.click()
                #clearworkspace()
                findelements()
            #else:
                #clearworkspace()
try:
#clearworkspace()
    findelements()
except:
    print ("Error occured")
    library = driver.find_element_by_id("library")
    elementsnamechecklist = library.find_elements_by_class_name("element")
    for elementsnamecheck in elementsnamechecklist:
        print(elementsnamecheck.find_element_by_class_name("elementName").text)
    print ("-----")
    print (driver.find_element_by_class_name("new-element-image-container").find_element_by_tag_name("img").get_attribute("alt"))

finally:
    driver.quit()
