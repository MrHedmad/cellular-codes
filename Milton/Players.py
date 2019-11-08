import time
import math
import random


class player:

    def __init__(self):
        # Coins -------------------------
        self.coinAmount = 0  # Current amount of coins
        self.bank = 100  # Maximum amount of coins
        self.coinBeforeHarvest = 0
        # Remembers the number of coins before an harvest
        self.lastHarvest = 0  # Remembers the number of coins last harvested
        # Generator --------------------
        self.generatorBase = 0.01  # Base coins/sec
        self.generatorBonus = 0.005  # Summed to the generatorBase
        self.generatorBonusBase = 1.10
        # Mult for generatorBonus when aumentaprod
        # Time -------------------------
        self.timeLastHarvest = time.time() - 300  # Time OF last harvest
        self.timeSinceLastHarvest = 0  # Time SINCE last harvest
        # Costs ------------------------
        self.costIncreaseBankMult = 1.10  # Cost increase for increasing bank
        self.costLastIncreaseBank = 0  # Last cost of increase Bank
        self.costLastMoreProd = 0  # Last cost increase Production
        self.costIncreaseBank = 90  # Cost of increasing bank
        self.costMoreProd = 100  # Cost of increasing production
        self.costIncreaseAtk = 100  # Cost of increasing atk
        self.costIncreaseArmor = 1000  # Cost of increasing armor
        self.costResurrect = self.bank * 0.50  # Cost of resurrecting
        # Stats ------------------------
        self.hp = 100  # Current HP
        self.maxHp = 100  # Max HP
        self.atk = 10  # Current attack
        self.armor = 5  # Current armor
        self.exp = 0  # Current experience
        self.deathState = "alive"  # Death status: alive or dead
        self.regenHp = 0.0013888  # Hp regen per second, equal to 5hp/hour
        self.timeOfDeath = None
        self.lastAttackTime = time.time()

    ##########################################################################
    def harvest(self):
        """Harvest coins after waiting some time. Returns false if harvesting
        fails, returns true if harvesting was a success."""
        # Calculate seconds since last harvest
        timeNow = time.time()
        timeSinceLast = timeNow - self.timeLastHarvest

        if timeSinceLast < 300:
            return False

        self.timeLastHarvest = timeNow
        self.timeSinceLastHarvest = timeSinceLast
        # Calculate the amount of coin matured
        randomFactor = max([min([random.gauss(mu=0.4, sigma=0.7), 2]), 1])

        self.lastHarvest = (self.timeSinceLastHarvest *
                            (self.generatorBase + self.generatorBonus) *
                            randomFactor)

        if self.deathState == "alive":
            self.coinBeforeHarvest = self.coinAmount
            self.coinAmount = min(self.coinAmount + self.lastHarvest,
                                  self.bank)
        else:
            self.coinBeforeHarvest = self.coinAmount
            self.coinAmount = min(self.coinAmount + (self.lastHarvest * 0.1),
                                  self.bank)

        days, hours, minutes, seconds = makereadable(self.timeSinceLastHarvest)

        phrase = ("Raccogli {d:.0f} giorni, {h:.0f} ore, {m:.0f}"
                  " minuti e {s:.0f} secondi di crescita, per un totale"
                  " di {lastHarvest:.2f} monete!"
                  ).format(d=days, h=hours, m=minutes, s=seconds,
                           lastHarvest=self.lastHarvest)

        # Signal coin update
        if self.coinBeforeHarvest + self.lastHarvest > self.bank:
            phrase += (" Peccato che non hai abbastanza spazio per tenere"
                       " tutte le nuove monete...\n")

        if self.deathState == "alive":
            # Hp Regen
            newHp = self.regenHp * timeSinceLast
            self.Hp = round(min(newHp, self.maxHp))

            phrase += ("\nRigeneri anche {0:.0f} Hp,"
                       " e hai ora un totale di {1} Hp.\n"
                       ).format(newHp, self.Hp)
        else:
            phrase += (" In questo momento sei morto. Puoi raccogliere solo"
                       " il 10% delle monete normali se sei morto.\n"
                       "Puoi tornare in vita con ?resuscita")

        return phrase

    ##########################################################################
    def totalCoinMessage(self):
        """Return message to move to chat when total money is asked"""
        return f"Hai {self.coinAmount:.2f} monete."

    ##########################################################################
    def currentStatusMessage(self):
        """Return various statistics for the game such as current coins and
        costs"""
        message = ""
        message += self.totalCoinMessage() + "\n"
        message += ("Le tue statistiche:\n"
                    "- Hp massimi: {maxHp};\n"
                    "- Hp correnti: {Hp};\n"
                    "- Attacco: {atk};\n"
                    "- Armatura: {armor};\n"
                    "\n"
                    "Dovrai pagare:\n"
                    "- {costBank:.2f} monete per aumentare lo spazio della"
                    " banca da {coinMax:.2f} a {futureCoinMax:.2f};\n"
                    "- {costProd:.2f} monete per aumentare la produzione di"
                    " monete al secondo del 10%;\n"
                    "- {costAtk:.2f} monete per aumentare l'attacco di 5;"
                    "- {costArmor:.2f} monete per aumentare l'armatura di 10;"
                    "- {costRes:.2f} monete per resuscitare."
                    "\n"
                    "Produci un totale di {coinProduction:.5f} monete"
                    " al minuto."
                    ).format(
            costBank=self.costIncreaseBank,
            coinMax=self.bank,
            futureCoinMax=(self.bank * self.costIncreaseBankMult),
            costProd=self.costMoreProd,
            coinProduction=(self.generatorBase + self.generatorBonus),
            maxHp=self.maxHp,
            Hp=self.hp,
            atk=self.atk,
            armor=self.armor,
            costAtk=self.costIncreaseAtk,
            costArmor=self.costIncreaseArmor,
            costRes=self.costResurrect
        )
        if self.deathState == "dead":
            message += ("\n In questo momento sei morto. Produci solo il"
                        " 10% delle monete normali.")
        return message

    ##########################################################################
    def increaseMax(self):
        if self.coinAmount < self.costIncreaseBank:
            return ("Non hai abbastanza monete ({coin:.2f}) per aumentare"
                    " il massimo. Te ne servono {cost:.2f}.").format(
                coin=self.coinAmount,
                cost=self.costIncreaseBank)

        self.costLastIncreaseBank = self.costIncreaseBank
        self.coinAmount -= self.costIncreaseBank
        # Core bank increase function. Multi last bank with MaxMult (1.10)
        self.bank *= self.costIncreaseBankMult
        self.bank = math.ceil(self.bank)
        self.costIncreaseBank = (self.bank *
                                 math.log(self.bank, self.bank * 1.25))

        return ("Hai speso {cost:.2f} monete per aumentare la grandezza della"
                " tua banca a {coinMax:.0f}. Dovrai spendere {costMoreMax:.2f}"
                " per farlo di nuovo.").format(
            cost=self.costLastIncreaseBank,
            coinMax=self.bank,
            costMoreMax=self.costIncreaseBank
        )

    ##########################################################################
    def increaseProd(self):
        if self.coinAmount < self.costMoreProd:
            return ("Non hai abbastanza monete ({coin:.2f}) per aumentare"
                    " la produzione. Te ne servono {cost:.2f}.").format(
                coin=self.coinAmount,
                cost=self.costMoreProd)

        self.costLastMoreProd = self.costMoreProd  # Remember
        self.coinAmount -= self.costMoreProd  # Remove cost
        self.costMoreProd **= 1.25  # Increase cost of bonus
        self.generatorBonus *= self.generatorBonusBase

        return ("Hai speso {cost:.2f} monete per aumentare la produzione"
                " di monete del 10%. Ora produci {coinProd:.3f} monete al"
                " secondo. Dovrai spendere {costMoreProd:.2f} per farlo"
                " di nuovo.").format(
            cost=self.costLastMoreProd,
            coinProd=(self.generatorBase + self.generatorBonus),
            costMoreProd=self.costMoreProd
        )

    ##########################################################################
    def increaseAtk(self):
        if self.coinAmount < self.costIncreaseAtk:
            return ("Non hai abbastanza monete ({coin:.2f}) per aumentare"
                    " l'attacco. Te ne servono {cost:.2f}.").format(
                coin=self.coinAmount,
                cost=self.costIncreaseAtk)

        lastCost = self.costIncreaseAtk  # Remember
        self.coinAmount -= self.costIncreaseAtk  # Remove cost
        self.costIncreaseAtk **= 1.15  # Increase cost of bonus
        self.atk += 5

        return ("Hai speso {cost:.2f} monete per aumentare il tuo attacco"
                " di 5. Ora hai {atk:.0f} attacco. Dovrai spendere"
                " {costIncreaseAtk:.2f} per farlo di nuovo.").format(
            cost=lastCost,
            atk=(self.atk),
            costIncreaseAtk=self.costIncreaseAtk)

    ##########################################################################
    def increaseDef(self):
        if self.coinAmount < self.costIncreaseArmor:
            return ("Non hai abbastanza monete ({coin:.2f}) per aumentare"
                    " l'armatura. Te ne servono {cost:.2f}.").format(
                coin=self.coinAmount,
                cost=self.costIncreaseArmor)

        lastCost = self.costIncreaseArmor  # Remember
        self.coinAmount -= self.costIncreaseArmor  # Remove cost
        self.costIncreaseArmor **= 1.17  # Increase cost of bonus
        self.armor += 10

        return ("Hai speso {cost:.2f} monete per aumentare la tua armatura"
                " del 10%. Ora hai {armor:.0f} armatura. Dovrai spendere"
                " {costIncreaseArmor:.2f} per farlo di nuovo.").format(
            cost=lastCost,
            armor=(self.armor),
            costIncreaseArmor=self.costIncreaseArmor
        )

    ##########################################################################
    def updateVariable(self, variable, value):
        setattr(self, variable, value)
        return f"Updated {variable} of player object to {value}"

    ##########################################################################
    def getAttacked(self, attack, targetName, attackerName):
        """Attacks this player.
        Returns in order message, deathstate and hp percentage"""

        if attack <= self.armor:
            return f"Non riesci neanche a scalfire l'armatura di {targetName}."
        else:
            self.hp -= attack - self.armor
            self.hp = max(self.hp, 0)
            damage = attack - self.armor
            message = (f"Colpito! Infliggi {damage} danni"
                       f"agli hp di {targetName}.")

        if self.hp == 0:
            self.deathState = "dead"
            self.timeOfDeath = time.time()
            gainedEXP = 100
            message += (" {0} ha ucciso {1}!"
                        "Hai guadagnato {2} esperienza.\n"
                        ).format(attackerName, targetName, gainedEXP)
            message += f"Hey, {targetName}. Ritorna in vita usando ?resuscita."

        return message, self.deathState, self.hp / self.maxHp * 100

    #########################################################################
    def checkAttackTime(self):
        timeDifference = time.time() - self.lastAttackTime

        if timeDifference >= 14400:
            # 14400 secs are 4 hours
            return True
        else:
            return False

    ##########################################################################
    def resurrect(self):
        if self.coinAmount < self.costResurrect:
            return ("Oh, no. Sei morto.\n"
                    "Non hai abbastanza monete ({coin:.2f}) per tornare in"
                    " vita. Te ne servono {cost:.2f}.").format(
                coin=self.coinAmount,
                cost=self.costResurrect)

        lastCost = self.costResurrect  # Remember
        self.coinAmount -= self.costResurrect  # Remove cost
        self.costResurrect = self.coinMax * 0.5  # Increase cost of bonus
        self.deathState = "alive"

        return ("Hai speso {cost:.2f} monete per tornare in vita."
                ).format(
            cost=lastCost,
            armor=(self.armor),
            costIncreaseArmor=self.costIncreaseArmor
        )


def makereadable(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = ((seconds % 86400) % 3600) // 60
    seconds = (((seconds % 86400) % 3600) % 60)
    return days, hours, minutes, seconds
