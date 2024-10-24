from generate import Generate
from translate import translate


class Morse():
    
    def Request(choice):

        if choice == "GENERATE":
            Generate()

        elif choice == "TRANSLATE":
            translate()
        
        else:
            print("INVALID RESPONSE")

def Input():

    choice = input("ENTER YOUR CHOICE : (GENERATE) , (TRANSLATE) : ")
    Morse.Request(choice)

Input()