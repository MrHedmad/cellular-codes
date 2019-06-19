import incremental as inc
import importlib
from tqdm import tqdm
import random

importlib.reload(inc)

gameSession = inc.game()
gameSession.addUser("luca")
gameSession.addUser("marco")

player = gameSession.getUser(username="luca")
player.harvest()

inc.save(gameSession)

inc.load("incSaveFile.pickle", gameSession)
player.totalCoinMessage()

for i in tqdm(range(int(1e8))):
    pass

with open("facts.txt", "r") as facts:
    lines = facts.readlines()
print(random.choice(lines))

a = 10
b = 20
