"""Demonstrate looping over a list argument by printing each text
message in a list of messages."""


def show_messages(text_messages):
    """Displays each text message"""
    for message in text_messages:
        print(f"\n{message}")


messages = ['hey, how are you?', 'good morning!',
            'sorry, i\'m running a bit late.', 'omg that\'s so crazy!']

show_messages(messages)
