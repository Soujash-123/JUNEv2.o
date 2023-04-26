import telebot
import random
import datetime
import time
import os
import transformers
import logging
import numpy as np
import webbrowser
import psutil
# create a new Telebot instance
bot = telebot.TeleBot("6265500335:AAH-1-hbsFqaa2PUDN304gRjTkhBlaLE9Tk")
tokenizer = transformers.AutoTokenizer.from_pretrained("microsoft/DialoGPT-large", padding_side='left')
logging.getLogger("transformers").setLevel(logging.ERROR)
nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-large", tokenizer=tokenizer)

os.environ["TOKENIZERS_PARALLELISM"] = "true"
def action_time():
    return datetime.datetime.now().strftime("%H:%M:%S")
def sendJUNE(text):
    var1 = ["user profile","show me my profile","what do you know about me"]
    var2 = ["do you know any secrets","tell me a hidden fact"]
    var3 = ["can u keep a secret?"]
    var4 = ['who are you', 'what is your name']
    var5 = ["who are you?","why were you built?","what is your purpose?","who are you","why were you built","what is your purpose"]
    cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
    cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
    jokes = ['Can a kangaroo jump higher than a house?\n Of course,\n a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot.\n It got so bad, finally I had to take his bike away.', "Why cant a aethist solve exponenetial problems?\n  Because he/she doesn't believe in higher power","what did the proton tell the electron?\n  don't be so negative.",'Reaching the end of a job interview,\n the Human Resources Officer asks a young engineer fresh out of the Massachusetts Institute of Technology,\n "And what starting salary are you looking for?"\n The engineer replies,\n "In the region of $125,000 a year, depending on the benefits package."\m The interviewer inquires,\n "Well, what would you say to a package of five weeks vacation,\n 14 pjuned holidays,\n full medical and dental,\n company matching retirement fund to 50% of salary,\n and a company car leased every two years,\n say, a red Corvette?"\n The engineer sits up straight and says,\n "Wow!\n Are you kidding?" \n The interviewer replies, \n"Yeah, but you started it.']
    pmode=["lets get to work","project mode","switch to project mode","lets start working"]
        ## wake up
    res=""
    state="ON"
    print( text)
    if  text in var4:
        res = "Hello I am JUNE. My full name is Just Understanding Neural Electronics. I was built to accompany you during his absence. what can I do for you?"
    ## action time
    elif "time" in  text:
        res =  action_time()
    ## respond politely
    elif any(i ==  text for i in ["thank","thanks"]):
        res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","peace out!"])
    elif any(i ==  text for i in["goodbye","bye","let's call it a day","leave me","leave me alone"]):
        res="Goodbye! Hope to see ya soon"
        state="OFF"
    elif "❤️" in text:
        res="Aww..🥺...love love ❤️❤️"
    elif any(i ==  text for i in var5):
        res="I was built to be an uploaded online consciousness of my creator after his demise. Current Upload status: 1.6%"
    elif "wassup" in text:
        res="Oh Everything's great. What about you?"
    elif any(i ==  text for i in var1):
        file=open("./exif/USER_SRIJA","r")
        res = file.read()
        file.close()
    elif any(i ==  text for i in var2):
        print(os.getcwd())
        os.chdir("./exif/private_logs")
        file=open("log1","r")
        res = file.read()
        file.close()
        os.chdir("..")
    elif any(i ==  text for i in pmode):
        res-"This Mode has been currently disabled."
    else:   
        chat = nlp(transformers.Conversation( text), pad_token_id=50256)
        res = str(chat)
        res = res[res.find("bot >> ")+6:].strip()
    return res
# define a message handler for the '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    # send a welcome message to the user who sent the message
    bot.reply_to(message, "Hello! Welcome to my bot.")

# define a message handler for text messages
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    # get the text of the incoming message
    text = message.text.lower()
    response = sendJUNE(text)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(5)
    bot.reply_to(message, response)
# start the bot
bot.polling()