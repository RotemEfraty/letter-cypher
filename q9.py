# Rotem Efraty, 349918219
def letterCypher(word, shiftNum):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wordFinal = ""

    for char in word:
        if char.isupper():
            if char in alphabet2:
                shiftedIndex = alphabet2.index(char) + shiftNum
                if shiftedIndex <= 25 and shiftedIndex >= -25:
                    wordFinal += alphabet2[shiftedIndex]
                elif shiftedIndex >= 25:
                    while shiftedIndex >= 25:
                        shiftedIndex = shiftedIndex - 26
                    wordFinal += alphabet2[shiftedIndex]
                elif shiftedIndex <= -25:
                    while shiftedIndex <= -25:
                        shiftedIndex = shiftedIndex + 26
                    wordFinal += alphabet2[shiftedIndex]
        elif char.islower():
            if char in alphabet:
                shiftedIndex = alphabet.index(char) + shiftNum
                if shiftedIndex <= 25 and shiftedIndex >= -25:
                    wordFinal += alphabet[shiftedIndex]
                elif shiftedIndex >= 25:
                    while shiftedIndex >= 25:
                        shiftedIndex = shiftedIndex - 26
                    wordFinal += alphabet[shiftedIndex]
                elif shiftedIndex <= -25:
                    while shiftedIndex <= -25:
                        shiftedIndex = shiftedIndex + 26
                    wordFinal += alphabet[shiftedIndex]
        else: 
            wordFinal += char
    return wordFinal

'''Encrypts letters inputted in "word" by shifting them by 
"shiftNum" on the alphabet'''

print(letterCypher("HelLo!", 3578))
