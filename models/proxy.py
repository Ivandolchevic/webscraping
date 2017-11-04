class Proxy:
    def __init__(self, reflected):
        self.value = reflected.value
        self.type = reflected.type
        self.success = reflected.success
        self.fails = reflected.fails
        self.lastsuccess = reflected.lastsuccess

    def getURL(self):
        return self.type + "://" + self.value

    def getIP(self):
        return self.value.split(':')[0]

    def getPort(self):
        return self.value.split(':')[1]

