# send one message to multiple persons. just switch the placeholder names.
# generated messages will be in 'Output/ReadyToSend'Folder
invited_names = open("./Input/Names/invited_names.txt")
starting_letter = open("./Input/Letters/starting_letter.txt")
starting_letter_text = starting_letter.read()

for name in invited_names:
    stripped_name = name.strip()
    # replace name of 'send to' with names of 'invited_names.txt'
    new_letter_replaced_send_to = starting_letter_text.replace("[PLACERHOLDER_SEND_TO]", stripped_name)
    # replace 'Angela placeholder' with name of sender
    new_letter_generated = new_letter_replaced_send_to.replace("[PLACEHOLDER_SENDER]", "Moritz")

    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as generated_letter:
        generated_letter.write(new_letter_generated)
        print(new_letter_generated)
