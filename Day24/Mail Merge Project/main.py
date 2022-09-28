with open("Input/Letters/starting_letter.txt", "r") as letters:
    content = letters.read()
    print(content)

with open("Input/Names/invited_names.txt", "r") as names:
    lines = names.readlines()
    for line in lines:
        strippedline = line.strip()
        with open(f"Output/ReadyToSend/letter_for_{strippedline}.txt", "w") as output:
            output.write(content.replace("[name]", strippedline))
