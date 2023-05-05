import telebot
import openai


#Bot Api Token
API_TOKEN = '6088288119:AAGyNiKIZE-3LbNsF707iLB2CCYHS4fvqd8'
#Openai Api Key
openai.api_key="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"
#Bot by @PEGASUSxIO

bot = telebot.TeleBot(6088288119:AAGyNiKIZE-3LbNsF707iLB2CCYHS4fvqd8)

#Generate The Response
def get_response(msg):
	completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=msg,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
	return completion.choices[0].text

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	 # bot.send_message(message.chat.id,message.text)
	   bot.send_message(message.chat.id, """\
Hi there, I am A Ai ChatBot.
I am here to Give Answers Of Your Question.
I Am Created Using Chatgpt Api ! 
Use /ask  To Ask Questions\
""")

#Handle The '/ask'
@bot.message_handler(commands=['ask'])
def send_answer(message):
	question=message.text[len("/ask"):]
	if len(question)==0:
		bot.send_message(message.chat.id,"Send Like This /ask Your Question") 
	else:
		bot.send_message(message.chat.id,get_response(question))


#run the Bot
bot.infinity_polling()