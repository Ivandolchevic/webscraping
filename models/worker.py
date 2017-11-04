import random
import sys
from threading import Thread
import time
from models.context import Context
from models.workflows import Workflows
from models.workflow import Workflow
from utils.webutil import ConnectionTimeoutError
import utils.logutil as logger
import utils.fileutil as file
from models.exceptions import NavigationFailed

class Worker(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, identifier, inputs):
        Thread.__init__(self)
        self.identifier = str(identifier)
        self.workflows = Workflows(inputs)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        logger.log("main()", "infos", "worker " + self.identifier + " start ...")

        # create a directory for the results 
        file.mkdir("tmp/worker_" + self.identifier)
                
        try:
            for _ in range(len(self.workflows.list)):
                w = self.workflows.getNextWorkflow()
                for _ in range(len(w.actions)):
                    action = w.getNextAction()
                    action.do()
            
            logger.log("main()", "success", "worker " + self.identifier + " finished !")

        except NavigationFailed as e:        
            ctx = self.workflows.context
            ctx.proxies.setScoreFails(ctx.proxy)
            logger.log("main()", "error", "worker " + self.identifier + ": " + e.message)       
        finally:
            try:
                ctx.driver.close()     
            except e:
                logger.log("main()", "error", "driver cannot be closed: " + e.message)   

    