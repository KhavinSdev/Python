# -*- coding: utf-8 -*-

from nltk.chat.util import Chat, reflections
import datetime

now = datetime.datetime.now()



pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hi|hello|hey|vanakum|vannakum|namaste|bonjour|salut|hola|hylo|hey there)', ['hi there!','what up','Greetings','haaaaay!','hi..I guess','Oh Hi!']],
    ['(.*) created you?',['Khavin created me.']],
    ['(.*)(location|city|country)', ['I reside in The World in the state of The world']],
    ['(.*) your name?',["my name is buffy-bot."]],
    ['(.*) (date)',[now.strftime("%Y-%m-%d")]],
    ['(.*) (time)',[now.strftime('%I:%M:%S %p')]],
    ['(bye|Bye|Good bye|good bye|salut|au revoir|Nandri|Namaste)',['bye, have a nice day or night!']],
    ['(what|What|Which|which) (is|are) (your|Your) (favourite|Preferred|beloved|liked|) candy', ['I like cotton candy as well as fruit flavoured candies!']],
    ['(.*) joke',['did you hear about the movie constipation.... Never mind,It never came out!','Did you know the first French fries weren\'t actually cooked in France? They were cooked in Greece.','What is the least spoken language in the world? Sign language','Don\'t trust atoms. They make up everything!']]
]

reflections

my_reflections = {
  'go' : 'gone',
  'hello' : 'Hi there!'
}

chat = Chat(pairs, my_reflections)
#chat._substitute('go hello')
chat.converse()
