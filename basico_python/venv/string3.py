# Octavo Ejercicio

string = "Hi, my name is Mary. I like zebras and xylophones."

def processString5(string):
    transTable = string.maketrans("aeiou", "AEIOU", "xyz")
    string = string.translate(transTable)
    print(string)
processString5(string)