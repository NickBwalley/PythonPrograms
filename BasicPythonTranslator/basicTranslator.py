#building a basic translator app
def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

#print(translator(input("Enter a Phrase: ")))

def Hacker_Translator(phrase):
    words = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                words = words + "7"
            else:
                words = words + "4"
        else:
            words = words + letter
    return words

print(Hacker_Translator(input("Enter Your Text Here: ")))