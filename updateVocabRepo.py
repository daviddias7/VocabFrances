import pandas as pd

# The key uniqueness is in the wordFrench column, so it's not possible to have two entries with the same French word.

# Keeps asking the user for new register entries, and updates "registerFILE" with the new entries,
# until the user enters the $ character.

# The register is a csv file with the following columns:
# wordFrench, wordEnglish, wordPortuguese,
# nDaysReviewed, nDaysLastReview,
# nDaysCorrect, nDaysLastCorrect,

# The 3 first columns are the words in French, English and Portuguese, requested from user
# All the other columns are automatically updated by the program (vocab.py), but initially they are all 0 (in this file, updateVocabRepo.py)

def get_fileName():
    fileName = input("Enter the name of the file to be updated (without the .csv extension): ")
    return fileName + ".csv"

columns = ('wordFrench', 'wordEnglish', 'wordPortuguese', 'nDaysReviewed', 'nDaysLastReview', 'nDaysCorrect', 'nDaysLastCorrect') 
word = ["", "", ""]

fileName = get_fileName()
# registerFILE = pd.read_csv(fileName, index_col=0)

# Explains to the user the code:
print("This program will ask you for new register entries, and update the file", fileName, "with the new entries.")
print("Type $, in the French word field, to stop.\n")

while True: 
    
    word[0] = input("French word/expression: ")
    if word[0] == "$":
        break
    word[1] = input("English word/expression: ")
    word[2] = input("Portuguese word/expression: ")

    # Shows the new register entry
    print("New register entry: ", word)

    # Asks if it's right, and if it's not, doesn't update the register
    answer = input("Is this right? (y/n) ")

    if answer == "y":

        newRegister = pd.DataFrame([word + [0, 0, 0, 0]], columns=columns)
        newRegister.to_csv(fileName, mode='a', header=False, index = False)
        print("Register updated.\n")

    else:
        print("Register not updated.\n")
        continue
