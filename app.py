from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Anvesha")
bot.set_trainer(ListTrainer)
bot.train(['What is your name?', 'My name is Anvesha'])
bot.train(['Who are you?', 'I am a bot' ])
bot.train(['Who created you?','Yash Kumar Arora', 'You?'])
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()
