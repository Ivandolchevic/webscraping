from models.context import Context
from models.workflows import Workflows
from models.workflow import Workflow
from models.exceptions import NavigationFailed
from models.worker import Worker 
from utils.webutil import ConnectionTimeoutError
import utils.logutil as logger
import utils.fileutil as file



# Création des threads
inputs = ["Guillaume", "COUQUET"]

threads = []
for i in range(4):
    threads.append(Worker(i, inputs))

# Lancement des threads
for thread in threads:
    thread.start()

# Attend que les threads se terminent
for thread in threads:
    thread.join()

"""
while True:
    ws = Workflows(["Guillaume", "COUQUET"])

    try:
        for _ in range(len(ws.list)):
            w = ws.getNextWorkflow()
            for _ in range(len(w.actions)):
                action = w.getNextAction()
                action.do()

        break;
    except NavigationFailed as e:        
        ctx = ws.context
        ctx.proxies.setScoreFails(ctx.proxy)
        logger.log("main()", "error", e.message)
    

print(ws.context.results)
"""