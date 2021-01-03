print("Welcoe to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = (bill*(int(input("Would percentage tip would you like to leave 10%, 12% or 15%?\n"))/100))
total=bill+tip
friends = int(input("How many people are going to split the bill?\n"))
print(f"Each one should pay: {round(total/friends,2)}$.")