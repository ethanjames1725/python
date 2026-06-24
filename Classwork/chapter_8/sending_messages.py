"""summary"""


def show_messages(text_messages):
    """Displays each text message"""
    for message in text_messages:
        print(message)


def send_messages(text_msgs):
    """Displays each text message and moves each message to a new list."""

    while text_msgs:
        current_message = text_msgs.pop()
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages


messages = ['hey, how are you?', 'good morning!', 'omg that\'s so crazy!',
            'sorry, i\'m running a bit late.', 'what you up to?']
sent_messages = []

send_messages(messages)

print(messages)
print(sent_messages)
