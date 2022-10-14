complete_letters = []
i = 0
with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()

for name in names:
    complete_letters.append(starting_letter.replace("[name]", name))

for complete_letter in complete_letters:
    with open(f"Output/ReadyToSend/{names[i]}.txt", "w") as file:
        file.write(complete_letter)
        i += 1


print(starting_letter)
print(names)
print(complete_letters)
