from replit import clear
import random
import words
import art

chosen_word = random.choice(words.word_list)
lives = 6

print(art.logo)

display = []
wrong_letters=[]
for i in chosen_word:
  display.append("_")

game = True

while game:
    if len(wrong_letters)>0:
        print(f"Wrong Guessed Letters : {wrong_letters}")
    guess = input("\nGuess a letter: ").lower()
    clear()
    if guess in display or guess in wrong_letters:
        print(f"You have already guessed the letter '{guess}''")
    elif guess in chosen_word:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guess:
                display[letter]= guess
    else:
        lives-=1
        wrong_letters.append(guess)

    print(display)
    print(art.stages[lives])
    if "_" not in display and lives>0:
        print ("You win!")
        game = False
    elif "_" in display and lives == 0:
        print(f"You lose.\nThe word was {chosen_word}")
        game= False
