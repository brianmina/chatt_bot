# bot.py

from chatterbot import ChatBot
from chatterbot.logic.logic_adapter import LogicAdapter
from chatterbot.preprocessors import *
from chatterbot.storage import StorageAdapter
from cleaner import clean_corpus
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer

# chatbot.storage.drop() #.... only for reset the db.

basic_conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot = ChatBot("TARS")
trainer = ListTrainer(chatbot)
trainer.train(basic_conversation)


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")