###littlealch.py
###Author: Joe Meier; joelmeier08@gmail.com

###Imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException
import time

###Start and Steup
driver = webdriver.Firefox()
driver.get("https://littlealchemy2.com/")
driver.maximize_window()
time.sleep(0.5)
play = driver.find_element_by_class_name("loading-screen-container")
play.click()
print ("start")

def isnewelement(newelementcontainer):
    library = driver.find_element_by_id("library")
    elementsnamechecklist = library.find_elements_by_class_name("element")
    new = True
    try:
        for elementsnamecheck in elementsnamechecklist:
            elemnamecheckname = elementsnamecheck.find_element_by_class_name("elementName")
            name_to_check = newelementcontainer.find_element_by_tag_name("img").get_attribute("alt")
            print ("element in list: " + str(name_to_check) + " is checked whit " + str(elemnamecheckname.text))
            if str(name_to_check) == str(elemnamecheckname.text):
                new = False
        return new
    except NoSuchElementException:
        return False
    return True

#def clearworkspace():
#    settings.click()
#    time.sleep(0.25)
#    cleanup = driver.find_element_by_xpath("//*[contains(text(), 'clean up')]")
#    cleanup[0].click()
#    time.sleep(0.25)

def findelements():
    library = driver.find_element_by_id("library")
    elements = library.find_elements_by_class_name("element")
    for elem in elements:
        elemname = elem.find_element_by_class_name("elementName")
        elempic = elem.find_element_by_tag_name("img")
        for elem2 in elements:
            elempic2 = elem2.find_element_by_tag_name("img")
            elemname2 = elem2.find_element_by_class_name("elementName")
            workspace = driver.find_element_by_id('workspace')
            y_position = 0
            searching = True

            while searching:
              try:
                ActionChains(driver).drag_and_drop(elempic, workspace).perform()
                searching = False
              except MoveTargetOutOfBoundsException:
                y_position += 500
                driver.execute_script('window.scrollTo(0, ' + str(y_position) + ');')
              print ('Element 1 dragged: ' + str(elemname.text))
##            try:
##                ActionChains(driver).drag_and_drop(elempic, workspace).perform()
##            except MoveTargetOutOfBoundsException:
##                print ("Need to Scroll because if element 1")
##                ActionChains(driver).move_to_element(elempic).perform()
##                ActionChains(driver).drag_and_drop(elempic, workspace).perform()
##            print ("Element 1 dragged: " + str(elemname.text))

            y_position = 0
            searching = True

            while searching:
              try:
                ActionChains(driver).drag_and_drop(elempic2, workspace).perform()
                searching = False
              except MoveTargetOutOfBoundsException:
                y_position += 500
                driver.execute_script('window.scrollTo(0, ' + str(y_position) + ');')
                driver.execute_script("window.scrollTo(0, arguments[0])", location.get('y'))
              print ('Element 2 dragged: ' + str(elemname2.text))

##            try:
##                ActionChains(driver).drag_and_drop(elempic2, workspace).perform()
##            except MoveTargetOutOfBoundsException:
##                print ("Need to Scroll because if element 2")
##                ActionChains(driver).move_to_element(elempic2).perform()
##                ActionChains(driver).drag_and_drop(elempic2, workspace).perform()
##            print ("Element 2 dragged: " + str(elemname2.text))
            time.sleep(1)
            newelementcontainer = driver.find_element_by_class_name("new-element-image-container")
            if isnewelement(newelementcontainer):
                print ("new element")
                newelementname = newelementcontainer.find_element_by_tag_name("img").get_attribute("alt")
                print (str(elemname.text) + "+" + str(elemname2.text) + "=" + str(newelementname) + ".")
                newelementcontainer.click()
                findelements()

try:
    findelements()
    print ("all elements done")
except  Exception as e:
    print ("Exception:")
    print(e)
    print ("Information on Elements:")
    library = driver.find_element_by_id("library")
    elementsnamechecklist = library.find_elements_by_class_name("element")
    for elementsnamecheck in elementsnamechecklist:
        print(elementsnamecheck.find_element_by_class_name("elementName").text)
    print ("-----")
    print (driver.find_element_by_class_name("new-element-image-container").find_element_by_tag_name("img").get_attribute("alt"))
finally:
    driver.quit()
