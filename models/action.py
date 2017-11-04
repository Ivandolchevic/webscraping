from models.actionmaker import ActionMaker
import utils.logutil as logger

class Action:    
    def __init__(self, dictionary,context):
        self.name = dictionary.get("name")
        self.method = dictionary.get("method")
        self.criteria = dictionary.get("criteria")        
        self.result = dictionary.get("result")
        self.context = context

        if "input" in dictionary:   
            self.initInput(dictionary.get("input"))
        else:
            self.input = None

        if "root" in dictionary:   
            self.root = dictionary.get("root")
        else:
            self.root = "driver"


    def initInput(self, value):
        if value.startswith(":VAR_CONTEXT_"):
            index = int(value.replace(":VAR_CONTEXT_",""))            
            self.input = self.context.inputs[index]
        else:
            self.input = value
        
        
    def do(self):
        logger.log("action.do()", "infos", "executing the action " + self.name + " ...")
        """ Execute the action """ 
        # initialize a new action maker
        amaker = ActionMaker(self, self.context)

        # launch the action maker
        result = amaker.start()

        logger.log("action.do()", "infos", "action " + self.name + " finished!")

        return result

    