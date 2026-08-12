import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO:
# 1. Convert dataframe to dictionary

nato_phonetic_alphabet = {row.letter: row.code  for (index, row) in data.iterrows()}

# 2. Ask user for a word
user_input = input("What is the word: ").upper()
# 3. Generate NATO code words using list comprehension
try:
    phonetic_words = [nato_phonetic_alphabet[letter] for letter in user_input]
# 4. Print the result
    print(phonetic_words)
except KeyError:
    print("Sorry, only letters in the alphabet please.")

