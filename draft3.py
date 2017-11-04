from models.proxies import Proxies
from models.proxy import Proxy

import utils.webutil as web
import utils.configutil as config
import utils.contextutil as context
import utils.maputil as mapper
import utils.logutil as logger
import utils.fileutil as files


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# load proxies 
proxies = Proxies(config.getProxiesFiles(), web.getProtocol(context.getCurrentURL()))

for _ in range(1):
    # get a proxy
    proxy = Proxy(mapper.json2obj(proxies.GetRandom()))

    driver = None

    # wait until the first field is available
    #try:
    driver = web.getFirefoxDriver(proxy)        

    # navigate to the url
    web.navigateURL(context.getCurrentURL(), driver)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txtMail"))
    )

    time.sleep(2)

    logger.log("wait()", "success", "element " + "txtMail" + " detected")
        
    # fill the email
    web.fillField(driver, "txtMail", "hervedupont2017@laposte.net")

    # fill the password
    web.fillField(driver, "pwdPassAuth", "Generic@0",True)

    print(type(driver.page_source))
    print(driver.page_source)
    proxies.setScoreSuccess(proxy)


    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "jTrackSearchHeader"))
    )

    searchLinkContainer = driver.find_element_by_id("jTrackSearchHeader")
        
    searchLink = searchLinkContainer.find_elements_by_tag_name("a")
    searchLink[0].click()
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txtVille"))
    )
    
    # fill the firstname
    web.fillField(driver, "txtPrenom", context.getFirstname())
    
    # fill the lastname
    web.fillField(driver, "txtNom", context.getLastname(),True)

    # waiting for the results page    
    logger.log("main()", "infos", "waiting for the search results ...")
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "app_list--result__search"))
    )
    
    logger.log("main()", "infos", "finding list of results ...")

    # get the list of results
    ul = driver.find_element_by_class_name("app_list--result__search")
    ul_lis = ul.find_elements_by_tag_name("li")

    logger.log("main()", "infos", "extract the list of urls toward the profiles ...")

    # get links urls
    all_links = []

    for li in ul_lis:
        li_h3 = driver.find_element_by_tag_name('h3')
        if li_h3 != None:
            li_h3_a = li_h3.find_element_by_tag_name('a')        
            if li_h3_a != None:
                all_links.append(li_h3_a.get_attribute("href"))


    # files.save(driver.page_source)

    logger.log("main()", "success", "All treatments finished successfully")
    """
    except:
        logger.log("wait()", "error", "proxy " + proxy.value +  "fails")
        proxies.setScoreFails(proxy)
    finally:    
        if driver != None:
            driver.quit()
"""

