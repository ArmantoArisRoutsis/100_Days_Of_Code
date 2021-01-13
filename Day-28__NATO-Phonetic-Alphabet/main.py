import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_data = {row.letter:row.code for (index,row) in data.iterrows()}

word = input("Enter a word: ").upper()

for i in word:
    print(f"{i} as {new_data[i]"}