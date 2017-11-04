from selenium import webdriver
import time

url = "https://copainsdavant.linternaute.com"

browser = webdriver.Chrome()
browser.get(url)

time.sleep(10)
html_source = browser.page_source

webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

# you have to use remote, otherwise you'll have to code it yourself in python to 
driver = webdriver.Remote(url, webdriver.DesiredCapabilities.CHROME)


