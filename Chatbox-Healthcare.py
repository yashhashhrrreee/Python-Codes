from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize the chatbot
chatbot = ChatBot("Healthcare Chatbot")

# Train the chatbot with your own data
trainer = ListTrainer(chatbot)

# Define your conversational data
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you",
    "You're welcome.",
    "What is your favorite color?",
    "I don't have a favorite color.",
    "What do you like to do?",
    "I like to chat with people.",
    "What is your favorite food?",
    "I don't have a favorite food.",
    "What do you do for a living?",
    "I am a healthcare chatbot."
]

# Train the chatbot with the conversational data
trainer.train(conversation)

# Start a conversation with the chatbot
while True:
    request = input("You: ")
    response = chatbot.get_response(request)
    print("Chatbot: ", response)
