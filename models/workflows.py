import utils.configutil as config
from models.workflow import Workflow
from models.context import Context
from utils.fileutil import openJSON

class Workflows:
    def __init__(self,inputs):
        self.file = config.getWorkflowsFile()
        self.list = openJSON(self.file)      
        self.current = -1
        self.context = Context(inputs)
        
    def getNextWorkflow(self):
        self.current += 1 
        return Workflow(self.list[self.current],self.context)

    def getSize(self):
        return len(self.list)
