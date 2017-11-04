from selenium import webdriver
import utils.logutil as logger
from selenium.webdriver.common.proxy import *

def getProtocol(url):
    return url.split("://")[0]

"""
def navigateURL(url, proxy):
    logger.log("navigateURL()", "infos", "navigate to " + url + " through the proxy " + proxy.value  + " ...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy.value)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    logger.log("navigateURL()", "success", url + " opened.")
    return driver
"""

class ConnectionTimeoutError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def navigateURL(url, driver):
    logger.log("navigateURL()", "infos", "navigate to " + url + " ...")    
    try:
        driver.get(url)
        logger.log("navigateURL()", "success", url + " opened.")
    except:
        logger.log("navigateURL()", "error", url + " nothing opened.")    
        raise ConnectionTimeoutError("Connection timeout error")    
    return driver

def fillField(driver, id, value,submit=False):    
    """ fill the given fild with the given value """
    logger.log("fillField()", "infos", "filling the field " + id + " with the value " + value  + " ...")
    inputField = driver.find_element_by_id(id)
    inputField.send_keys(value)
    logger.log("fillField()", "success", "The field " + id + " has been filled with the value " + value)

    if submit:
        return inputField.submit()
    else:
        return None

def getFirefoxDriver(proxy):        
    PROXY_HOST = proxy.getIP()
    PROXY_PORT = proxy.getPort()
    logger.log("getFirefoxDriver()", "infos", "defining the firefox driver with proxy " + PROXY_HOST  + ":" + PROXY_PORT + " ...")
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http",proxy.getIP())
    fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.https",PROXY_HOST)
    fp.set_preference("network.proxy.https_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.ssl",PROXY_HOST)
    fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.ftp",PROXY_HOST)
    fp.set_preference("network.proxy.ftp_port",int(PROXY_PORT))
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))
    fp.set_preference("http.response.timeout", 20)
    fp.set_preference("dom.max_script_run_time", 20)
    # fp.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
    fp.update_preferences()
    
    logger.log("getFirefoxDriver()", "success", "firefox driver initialised")
    driver = webdriver.Firefox(firefox_profile=fp)    

    return driver