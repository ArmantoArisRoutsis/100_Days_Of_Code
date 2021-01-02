from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
answer = "yes"

def caesar(direction):
    new_word = ""
    for i in text:
        if i in alphabet:
            if(direction=="encode"):
                if alphabet.index(i) + shift > len(alphabet)-1:
                    new_word += alphabet[(alphabet.index(i) + shift)-(len(alphabet))]
                else:
                    new_word += alphabet[alphabet.index(i) + shift]
            elif(direction=="decode"):
                if alphabet.index(i) - shift < 0:
                    new_word += alphabet[(alphabet.index(i) - shift)+(len(alphabet))]
                else:
                    new_word += alphabet[alphabet.index(i) - shift]
        else:
          new_word+=i

    print(new_word)

while answer == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift%len(alphabet)

    caesar(direction)
    answer = input("Would you like to continue using this program? :").lower()