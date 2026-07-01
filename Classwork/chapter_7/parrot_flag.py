"""
Prompts the user for input and repeats it back to them until they enter
'quit'. It demonstrates the use of a while loop to continuously ask for input
and process it until a specific condition is met using a flag.
"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
