import random

print("Welcome to the Band Name Generator!")
first = []
first.append(input("\nWhat is the name of the city you grew up in?\n"))
first.append(input("\nWhat is your favourite color?\n"))
first.append(input("\nWhat is your least favourite color?\n"))
first.append(input("\nHow are you feeling at the moment?\n"))
first.append(input("\nWhich one is your favorite season?\n"))
second = []
second.append(input("\nWhat is your favourite animal?\n"))
second.append(input("\nWhat is your favourite food?\n"))
second.append(input("\nWhat is your current occupation?\n"))
bandName = first[random.randint(0,len(first)-1)]+" "+second[random.randint(0,len(second)-1)]
print("Your band name is ..."+bandName+"s!")