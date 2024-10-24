import random
from Morse import morse
from translate import translate

GeneratedString = ""

def Generate():

    global GeneratedString 

    num = random.randint(5,25)

    ListOfMorse = list(morse)
    random.shuffle(ListOfMorse)

    NumOfCommas = random.randint(2,5)

    for i in range(0 , num):
        GeneratedString = GeneratedString + ListOfMorse[i] + " "

    GeneratedString = list(GeneratedString)

    for i in range(0,NumOfCommas):
        GeneratedString.append(" , ")

    random.shuffle(GeneratedString)
    GeneratedString = ''.join(GeneratedString)

    print("String succesfully generated")

    translate()