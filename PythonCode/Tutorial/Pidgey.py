import math
poke = input("What pokemon are you evolving?: ")
candy = int(input("How many candies do you have?: "))
captured = int(input("How many pokemons do you already own?: "))

pokedex = {"Pidgey": 12, "Spheal": 25}

req = pokedex[poke]
result = math.floor(candy / req)
leftover = candy % req
newcandy = result * 4 + leftover
while newcandy > req:
    result = result + math.floor(newcandy / req)
    leftover = newcandy % req
    newcandy = math.floor(newcandy / req) * 4 + leftover

result = result - captured
print("You will need to catch ", result, " ", poke, ".\n",
      "And you will have ", leftover, " candies left when you finish.",
      sep="", end="")
