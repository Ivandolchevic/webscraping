from models.proxies import Proxies
from models.proxy import Proxy

import utils.configutil as config
import utils.maputil as mapper
import utils.webutil as web

class Context:
    def __init__(self, inputs):
        # http could be replaced by getProtocol(url)
        self.proxies = Proxies(config.getProxiesFiles(), "http")
        self.proxy = Proxy(mapper.json2obj(self.proxies.GetRandom()))
        self.driver = web.getFirefoxDriver(self.proxy)        
        self.inputs = inputs
        self.element = None
        self.elements = None
        self.results = None
