#python



!pip install adafruit-io

x = "yashikadevadiga" #ADAFRUIT_IO_USERNAME
y = "aio_aUEB49N1xmB0sQ63cFYi2FUnq63n" #ADAFRUIT_IO_KEY

from Adafruit_IO import Client, Feed
aio = Client(x,y)

#create a new feed
new = Feed(name='bot4') #feed name is given
result = aio.create_feed(new)
result

from Adafruit_IO import Data

#sending a value to afeed
value =Data(value=0)
value_send = aio.create_data('bot4',value)

!pip install python-telegram-bot

from telegram.ext import Updater,CommandHandler
import requests  # Getting the data from the cloud

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light turned on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    from Adafruit_IO import Data
    value = Data(value=1)
    value_send = aio.create_data('bot4',value)
 
def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning off'
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTuueKIndqjMG0rlzPZrO0UUFP6ts8b_CrUIQ&usqp=CAU'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=0)
    value_send = aio.create_data('bot4',value)
    
u = Updater('1260508901:AAG-l7pI-LzdzzcMjE0KxLsGrd7k-T7YYnY')  #change the token
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
