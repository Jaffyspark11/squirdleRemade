import random
import Pokemon
from Pokemon import dictOfPokemon as DOP

answer = Pokemon.listOfPokemon[random.randrange(801)].name
answer = answer.lower()
count = 0


def guess():
    global count
    guess = input("Guess a Pokemon: ")
    guess = guess.lower()
    if guess in DOP:
        if guess == answer:
            print("You Win!!!")
            exit()
        else:
            print(checkGen(guess) + ", " + checkType1(guess) + ", " + checkType2(guess) + ", " + checkStats(guess))
            print(str(8 - count) + ' guesses remaining.')
    else:
        count -= 1
        print('Pokemon Does Not Exist')
        print(str(8 - count) + ' guesses remaining.')


def checkGen(guess):
    x = DOP.get(guess)
    y = DOP.get(answer)
    if x.gen == y.gen:
        return 'Correct Gen'
    elif x.gen > y.gen:
        return 'Gen is Lower'
    else:
        return 'Gen is Higher'


def checkType1(guess):
    if DOP.get(guess).type1 == DOP.get(answer).type2:
        return "Swap to Type 2"
    if DOP.get(guess).type1 == DOP.get(answer).type1:
        return "Type 1 is Correct"
    else:
        return "Type is Incorrect"


def checkType2(guess):
    if DOP.get(guess).type2 == DOP.get(answer).type1:
        return "Swap to Type 1"
    if DOP.get(guess).type2 == DOP.get(answer).type2:
        return "Type 2 is Correct"
    else:
        return "Type is Incorrect"


def checkStats(guess):
    if DOP.get(guess).stats == DOP.get(answer).stats:
        return "Same Base Stats"
    elif DOP.get(guess).stats > DOP.get(answer).stats:
        return "Base Stats are Lower"
    else:
        return "Base Stats are Higher"


while count < 8:
    count += 1
    guess()
exit()
