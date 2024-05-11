import nltk
import random
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi there!", "Hello! How can I help?"]
    ],
    [
        r"how are you|how are you doing",
        ["I'm doing fine, thank you! How can I assist you today?", "I'm well, thank you! How about yourself?"]
    ],
    [
        r"what is your name|who are you",
        ["I am a simple chatbot created by OpenAI. What's your name?", "I'm a bot! How can I assist you today?"]
    ],
    [
        r"i'm (.*) doing good|i'm (.*) doing well",
        ["That's great to hear! How can I help you today?", "Good to know! What can I do for you today?"]
    ],
    [
        r"quit|exit",
        ["Goodbye, have a nice day!", "Bye! It was nice talking to you."]
    ]
]

# This function will start the chatbot
def chat():
    print("Hi! I'm a simple chatbot. If you want to exit, type 'quit'")
    # Create a chatbot
    chatbot = Chat(pairs, reflections)
    # Start conversation
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":
    chat()
