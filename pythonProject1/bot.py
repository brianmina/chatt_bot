# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus


CORPUS_FILE = "chat_brother.txt"

chatbot = ChatBot(
    "My ChatterBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ]
)
# chatbot.storage.drop() .... only for reset the db.
trainer = ListTrainer(chatbot)

cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(["hola",
               "ole",])
trainer.train(["hello",
               "que anda haciendo?",
               "diga un numero",
               "para que?"])
chatbot = ChatBot(
    "My ChatterBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ]
)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")