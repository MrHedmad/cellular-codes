import Players
import pickle
import re


class game():
    def __init__(self):
        self.userDict = {}

    def addUser(self, username):
        user = Players.player()
        self.userDict.update({str(username): user})
        return True

    def getUser(self, username):
        return self.userDict[str(username)]

    def getFuzzyUser(self, username):
        return [[self.userDict[key], key] for key in list(self.userDict.keys())
                if re.search(key, username)]

    def getUserList(self):
        return self.userDict.keys()

    def loadUserDict(self, dictionary):
        self.userDict = dictionary

    def updateAllPlayers(self, variable, value):
        for obj in self.userDict.values():
            obj.updateVariable(variable, float(value))
        return "Updated all players. Remember to save"


############################################################################
def save(gameObject):
    with open("savefile.bin", "wb") as file:
        pickle.dump(obj=gameObject.userDict, file=file)


def load(saveFile, gameObject):
    with open(saveFile, "rb") as file:
        savedDict = pickle.load(file)
        for key, player in savedDict.items():
            newPlayer = Players.player()
            for variable, value in player.__dict__.items():
                setattr(newPlayer, variable, value)
                savedDict[key] = newPlayer
        gameObject.loadUserDict(dictionary=savedDict)
