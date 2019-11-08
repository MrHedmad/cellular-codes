import discord
import Game as game
import random

USEROLES = False  # Change this to let MLA change user roles. Broken?

help = ("Ciao! Sono Milton Library Assistant. I miei comandi:\n"
        "- ?help -> Per avere questo messaggio\n"
        "- ?fact -> Per avere un fatto molto interessante (in inglese).\n"
        "- ?roll <numero> -> Per tirare un dado da <numero> facce, es:"
        " ?roll 20 tira un d20.\n"
        "\n"
        "I comandi per il gioco sono:\n"
        "\n"
        "- ?raccogli -> Per raccogliere soldi dopo aver aspettato.\n"
        "- ?espandi -> Per aumentare il massimo dei soldi.\n"
        "- ?aumentaprod -> Per aumentare del dieci percento le"
        " monete al secondo.\n"
        "- ?stats -> Per avere le statistiche di gioco.\n")

client = discord.Client()
gameSession = game.game()


def checkPlayer(author):
    if str(author) not in gameSession.getUserList():
        gameSession.addUser(username=author)
        game.save(gameSession)
        print(f"Added {author} to the game")
    else:
        pass


try:
    game.load("savefile.bin", gameSession)
    print("Loaded game file")
except FileNotFoundError:
    print("No savefile for Incremental game found.")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("with myself.")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    # Do not reply to yourself
    if message.author == client.user:
        return

    if message.content.startswith("?help"):
        await message.channel.send(help)

    if message.content.startswith("?raccogli"):
        checkPlayer(message.author)
        player = gameSession.getUser(username=message.author)
        harvest = player.harvest()
        if harvest is False:
            await message.channel.send("Hey! E' un pò presto per collezionare"
                                       " di nuovo. Aspetta almeno cinque"
                                       " minuti.")
        else:
            game.save(gameSession)
            await message.channel.send(harvest + "\n" +
                                       player.totalCoinMessage())

    if message.content.startswith("?espandi"):
        checkPlayer(message.author)
        player = gameSession.getUser(username=message.author)
        stdout = player.increaseMax()
        game.save(gameSession)
        await message.channel.send(stdout)

    if message.content.startswith("?aumentaprod"):
        checkPlayer(message.author)
        player = gameSession.getUser(username=message.author)
        stdout = player.increaseProd()
        game.save(gameSession)
        await message.channel.send(stdout)

    if message.content.startswith("?compra attacco"):
        checkPlayer(message.author)
        player = gameSession.getUser(username=message.author)
        stdout = player.increaseAtk()
        game.save(gameSession)
        await message.channel.send(stdout)

    if message.content.startswith("?compra armatura"):
        checkPlayer(message.author)
        player = gameSession.getUser(username=message.author)
        stdout = player.increaseDef()
        game.save(gameSession)
        await message.channel.send(stdout)

    if message.content.startswith("?fact"):
        with open("facts.txt", "r") as facts:
            lines = facts.readlines()
            random_fact = random.choice(lines)
        await message.channel.send(random_fact)

    if message.content.startswith("?roll"):
        number = int(message.content[6:])
        await message.channel.send(("Ho tirato un dado da {facce:d} facce"
                                    " e ho fatto... {risultato}.").format(
            facce=number,
            risultato=random.randint(1, number)
        ))

    if message.content.startswith("?stats"):
        checkPlayer(message.author)
        player = gameSession.getUser(username=message.author)
        await message.channel.send(player.currentStatusMessage())

    if message.content.startswith("?giocatori"):
        checkPlayer(message.author)
        playerList = gameSession.getUserList()
        await message.channel.send("I giocatori sono: " +
                                   str(list(playerList)))

    if message.content.startswith("?resuscita"):
        checkPlayer(message.author)
        player = gameSession.getUser(username=message.author)
        if player.deathState == "dead":
            await message.channel.send(player.resurrect())
        else:
            await message.channel.send("Non sei morto! Per ora...")

    if message.content.startswith("?attacca "):
        checkPlayer(message.author)
        player = gameSession.getUser(username=message.author)
        if player.checkAttackTime() is False:
            await message.channel.send(("Puoi attaccare solo una volta"
                                       " ogni quattro ore."))
        else:
            target = message.content.split(" ")[1]
            target = gameSession.getFuzzyUser(username=target)
            print(target)
            if target is None:
                stdout = ("Non ho capito bene chi vuoi attaccare. Può essere"
                          " che c'è un altro giocatore con lo stesso nome?")
                await message.channel.send(stdout)
            elif target[0].deathState == "dead":
                targetUsername = target[1]
                target = target[0]
                stdout = (f"{targetUsername} è già morto."
                          " Non puoi attaccarlo di nuovo."
                          " Però mutili il cadavere. Bravo!")
                await message.channel.send(stdout)
            else:
                targetUsername = target[0]
                target = target[1]
                targetObj = gameSession.getUser(username=targetUsername)
                stdout, deathstate, playerpercentage = \
                    targetObj.getAttacked(player.atk,
                                          targetUsername,
                                          message.author)
                if USEROLES is True:
                    if playerpercentage >= 80:
                        role = "HighHp"
                    elif playerpercentage >= 40:
                        role = "MidHp"
                    elif playerpercentage >= 0:
                        role = "LowHp"
                    elif playerpercentage == 0:
                        role = "dead"

                    gameRoles = ["HighHp", "MidHp", "LowHp", "Dead"]
                    targetUserObj = message.guild.get_member(targetUsername)
                    await targetUserObj.remove_roles(*gameRoles)
                    await targetUserObj.add_roles(role)

                await message.channel.send(stdout)

    if message.content.startswith("?master"):
        command = message.content.split(" ")
        if message.author == message.guild.owner:
            if command[1] == "updateplayer":
                player = gameSession.getUser(username=command[2])
                out = player.updateVariable(command[3], float(command[4]))
                await message.channel.send(out)

            if command[1] == "updateallplayers":
                out = gameSession.updateAllPlayers(command[2],
                                                   float(command[3]))
                await message.channel.send(out)

            if command[1] == "forcesave":
                game.save(gameSession)
                await message.channel.send("Forced Saving")

            if command[1] == "getdict":
                player = gameSession.getUser(username=command[2])
                await message.channel.send(str(player.__dict__))

            if command[1] == "getuserlist":
                await message.channel.send(gameSession.getUserList())

            if command[1] == "resetuser":
                gameSession.addUser(command[2])
                await message.channel.send(
                    "Successfully reset user {}".format(command[2]))

            if command[1] == "help":
                await message.channel.send(
                    ("Master commands: ?master <command> -> updateplayer"
                     " <username> <variable> <value>; updateallplayers"
                     " <variable> <value>; forcesave; getdict <username>;"
                     " getuserlist; help"))

        else:
            await message.channel.send(
                "https://media.giphy.com/media/5ftsmLIqktHQA/giphy.gif")

# Start game from cmd ------------------------------------------------------
# Import token from command line
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="bot token", type=str)
    args = parser.parse_args()

    client.run(args.token)
