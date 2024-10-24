import generate as g
from Morse import morse

def translate():
        
    actual = ""

    print("Give SPACE between each letter AND a COMMA between each word ")
    print("Type 'random' to randomly generate string ")


    string = str(input("Enter the sentense to translate : "))

    if string == "random" and g.GeneratedString != "":
        string = g.GeneratedString
        print("\n Randomly generated morse : ")
        print(string)

    for i  in string.split(" "):
        for j in morse:
            if i == j:
                actual = actual + morse[j]

    if string == "random" and g.GeneratedString == "":
        print("\n String Empty")

    else:
        print("\n Translated String : ")
        print(actual)