from replit import clear
from art import logo

print(logo)
print("\n*** Welcome to the blind biding ***\n")
people = []
go_on = "yes"

while go_on=="yes":

  name = input("What is your name? :")
  bid = int(input("What is the amount you want to bid? :$"))
  people.append({"name":name,"bid":bid})

  go_on = input("Is there another person that would like to bid?")
  clear()

print("\nThis is the list with all of the people that participated in this auction along with their bid\n")

winner = people[0]
for person in people:
  print(f"Name: {person['name']}\nBid: {person['bid']}$")
  if person["bid"]>winner["bid"]:
    winner = person

print(f"The winner of this auction is{winner['name']} who bid the amout of {winner['bid']}$!")