import pandas
from replit import clear

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_data = {row.letter:row.code for (index,row) in data.iterrows()}
go_on = ""
while go_on != "EXIT":
  word = input("Enter a word: ").upper()

  try:
    for i in word:
        print(f"{i} as {new_data[i]}")
  except KeyError:
    print("Please input a word")
  else:
    go_on = input("\nWould you like to input another word?\n(Type 'exit' to exit the program or anything else to continue): ").upper()
    clear()
