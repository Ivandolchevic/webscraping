import utils.logutil as logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webutil import ConnectionTimeoutError
from models.exceptions import NavigationFailed
import time

class ActionMaker:
    def __init__(self, action, context):
        self.action = action
        self.context = context

    def start(self):    
        methodname = self.action.name + " " + self.action.result + " " + self.action.method
        logger.log("ACTION [" + methodname + "]", "infos", "start ...")
        result = self.methods[methodname](self,self.getRootFromString(self.action.root))
        logger.log("ACTION [" + methodname + "]", "infos", "finished!")
        return result

    def clickById(self,root):
        """ click on the specified identifier """ 
        self.context.element = root.find_element_by_id(self.action.criteria)
        self.context.element = self.context.element.find_elements_by_tag_name("a")[0]
        self.context.element.click()
        return self.context.driver.page_source

    def clickElementByTagName(self,root):
        """ click on an element specified by its tag name """
        logger.log("clickElementByTagName()", "infos", "start with criteria [" + self.action.criteria + "] ...") 
        self.context.element = root.find_element_by_tag_name(self.action.criteria)
        self.context.element.click()
        logger.log("findElementsByTagName()", "success", "finished with criteria [" + self.action.criteria + "] ...")
        return self.context.element
        
    def findElementByClassName(self,root):
        """ find an element using its class name """ 
        self.context.element = root.find_element_by_class_name(self.action.criteria)    
        return self.context.element

    def findByClassName(self,root):
        """ find an element using its class name """ 
        self.context.element = root.find_element_by_class_name(self.action.criteria)    
        return self.context.element
    
    def findElementById(self, root):               
        """ fill the given fild with the given value """
        logger.log("findElementById()", "infos", "start with criteria [" + self.action.criteria + "] ...")
        self.context.element = root.find_element_by_id(self.action.criteria)        
        logger.log("findElementById()", "success", "finished with criteria [" + self.action.criteria + "] ...")
        return self.context.element

    def fillById(self,root):        
        """ fill the given fild with the given value """
        logger.log("fillById()", "infos", "filling the field " + self.action.criteria + " with the value " + self.action.input  + " ...")
        self.context.element = root.find_element_by_id(self.action.criteria)
        self.context.element = self.context.element.send_keys(self.action.input)    
        logger.log("fillById()", "success", "The field " + self.action.criteria + " has been filled with the value " + self.action.input) 
        return self.context.element

    def navigateByURL(self,root):        
        """ fill the given fild with the given value """
        logger.log("navigateByURL()", "infos", "navigates to " + self.action.criteria + " ...")
        # navigate to the url
        try:
            root.get(self.action.criteria)        
            logger.log("navigateByURL()", "success", "Page " + self.action.criteria + " opened") 
        except:
            logger.log("navigateByURL()", "error", "Page " + self.action.criteria + " not openened") 
            raise NavigationFailed("Failed to navigate to " + self.action.criteria)        
        return self.context.driver.page_source

    def submitById(self,root):        
        """ submit the given field """
        logger.log("submitById()", "infos", "submitting the field " + self.action.criteria + " ...")
        self.context.element = root.find_element_by_id(self.action.criteria)
        self.context.element.submit()
        logger.log("submitById()", "success", "The field " + self.action.criteria + " has been submitted") 
        return self.context.element

    def waitByClassName(self,root):
        """ wait the element specified by his class name """        
        logger.log("waitByClassName()", "infos", "start with criteria [" + self.action.criteria + "] ...")
        self.context.element = WebDriverWait(root, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.action.criteria)))
        logger.log("waitByClassName()", "success", "finished with criteria [" + self.action.criteria + "] ...")
        return self.context.element

    def waitById(self,root):
        """ wait the element specified by his identifier """     
        logger.log("waitById()", "infos", "start with criteria [" + self.action.criteria + "] ...")   
        self.context.element = WebDriverWait(root, 10).until(EC.presence_of_element_located((By.ID, self.action.criteria)))
        logger.log("waitById()", "success", "finished with criteria [" + self.action.criteria + "] ...")
        return self.context.element
    
    def findElementsByTagName(self, root):
        """ find all elements that matche with the given tag name """
        logger.log("findElementsByTagName()", "infos", "start with criteria [" + self.action.criteria + "] ...") 
        self.context.elements = root.find_elements_by_tag_name(self.action.criteria)
        logger.log("findElementsByTagName()", "success", "finished with criteria [" + self.action.criteria + "] ...")
        return self.context.elements
    
    def findForEachElementsByTagName(self, root):
        logger.log("findForEachElementsByTagName()", "infos", "start with criteria [" + self.action.criteria + "] ...") 
        results = [];
        for element in root:
            elt = element.find_element_by_tag_name(self.action.criteria)
            if  elt != None:
                results.append(elt)
        self.context.elements = results
        logger.log("findForEachElementsByTagName()", "success", "finished with criteria [" + self.action.criteria + "] ...")
        return self.context.elements
            
    def getAttributeValuesForEachElements(self, root):
        logger.log("getAttributeForEach()", "infos", "start with criteria [" + self.action.criteria + "] ...") 
        results = [];
        for element in root:
            elt = element.get_attribute(self.action.criteria)
            if  elt != None:
                results.append(elt)
        self.context.results = results
        logger.log("getAttributeForEach()", "success", "finished with criteria [" + self.action.criteria + "] ...")
        return self.context.elements
    
    def getRootFromString(self,root):
        if root == "element":
            return self.context.element
        elif root == "elements":
            return self.context.elements
        else:
            return self.context.driver

    methods = {        
        "fill element byid":fillById,
        "find element byclassname":findByClassName,
        "find elements bytagname":findElementsByTagName,
        "find element byid":findElementById,
        "findforeach elements bytagname":findForEachElementsByTagName,   
        "navigate element byurl":navigateByURL,
        "submit element byid":submitById,
        "wait element byid":waitById,
        "wait element byclassname":waitByClassName,                
        "getattributeforeach values byname":getAttributeValuesForEachElements,
        "click element bytagname":clickElementByTagName
        
    }

