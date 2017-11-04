from models.action import Action

class Workflow:
    def __init__(self, dictionary,context):
        self.name = dictionary.get("name")
        self.actions = dictionary.get("actions")
        self.context = context
        self.step = -1

    def getNextAction(self):
        self.step += 1 
        return Action(self.actions[self.step],self.context)

    def getSize(self):
        return len(self.actions)