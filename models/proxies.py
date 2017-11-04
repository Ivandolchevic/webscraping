from utils.fileutil import openJSON
from random import randint
import utils.logutil as logger
import utils.configutil as config

import time
import json

class Proxies:
    def __init__(self, proxiesfile,protocol):
        self.protocol = protocol
        self.file = config.getResourcesFolder() + proxiesfile[protocol]
        self.proxies = openJSON(self.file)                

    def GetRandom(self):        
        """ select a proxy randomly """
        logger.log("Proxies.GetRandom()", "infos", "select a random proxy ...")      
        index = randint(0,len(self.proxies) - 1)
        logger.log("Proxies.GetRandom()", "infos", "selected proxy : " + self.proxies[index]["value"])
        
        return self.proxies[index]
    
    def setScoreSuccess(self,proxy):            
        logger.log("Proxies.setScoreSuccess()", "infos", "increase the success score of the proxy " + proxy.value)              
                
        # add a success to the proxy
        for p in self.proxies:                              
            if p["value"] == proxy.value:
                logger.log("Proxies.setScoreSuccess()", "infos", "updating " + proxy.value + " ...")                      
                p["success"] = p["success"] + 1
                p["lastsuccess"] = time.time()
        
        # save the proxies file updated                              
        with open(self.file,"w") as file:
            json.dump(self.proxies, file)
            file.close()
        
        logger.log("Proxies.setScoreSuccess()", "success", "success score of the proxy " + proxy.value + " has been increased")  

    def setScoreFails(self,proxy):            
        logger.log("Proxies.setScoreFails()", "infos", "increase the fail score of the proxy " + proxy.value)              
                
        # add a success to the proxy
        for p in self.proxies:                              
            if p["value"] == proxy.value:
                logger.log("Proxies.setScoreFails()", "infos", "updating " + proxy.value + " ...")                      
                p["fails"] = p["fails"] + 1
        
        # save the proxies file updated                              
        with open(self.file,"w") as file:
            json.dump(self.proxies, file)
            file.close()
        
        logger.log("Proxies.setScoreFails()", "success", "fails score of the proxy " + proxy.value + " has been increased")              