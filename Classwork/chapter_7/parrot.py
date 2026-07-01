"""
Prompts the user for input and repeats it back to them until they enter
'quit'. It shows the use of a while loop to keep asking for input and
processing it until a specific condition is met.
"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
