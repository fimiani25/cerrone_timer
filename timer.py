import telepot
import time
import threading

class Thread_timer (threading.Thread):
    chat_id=''
    tempo_rimanente=0
    
    def __init__(self, threadID, name, counter, chat_, tempo_): 
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.chat_id=chat_
        self.tempo_rimanente=tempo_
      
      
    def run(self):
        while self.tempo_rimanente>0:
          bot.sendMessage(self.chat_id,"tempo rimanente "+str(self.tempo_rimanente)+" minuti")
          time.sleep(60)
          self.tempo_rimanente=self.tempo_rimanente-1
        if self.tempo_rimanente==0:
            bot.sendMessage(self.chat_id,"live finita")
            

    def add(self,add_t):
        self.tempo_rimanente=self.tempo_rimanente+add_t

    def stampa_tempo(self):
        bot.sendMessage(self.chat_id,"tempo rimannete "+str(self.tempo_rimanente)+" minuti")
        
    def stop(self):
        self.tempo_rimanente=0
        #bot.sendMessage(self.chat_id,"live finita")
        
thread1 = Thread_timer(1, "Thread-1", 1,'',0)
tempo_rimanente=0
def on_chat_message(msg):
    content_type, chat_type, chat_id=telepot.glance(msg)
    if content_type == 'text':
       name = msg["from"]["first_name"]
       print(msg)
    if msg['text'].startswith("/set"):
        msg["text"]=msg["text"].replace("/set ","");
        temp=int(msg['text'])
        
        tempo_rimanente=int(msg['text'])
        global thread1
        #thread1.stop()
        if thread1.is_alive():
            thread1.stop()
        
        thread1 = Thread_timer(1, "Thread-1", 1,chat_id,tempo_rimanente)
        thread1.start()

        #for t in range(int(msg['text'])):
         #   bot.sendMessage(chat_id,"tempo rimannete "+str(tempo_rimanente)+" minuti")
          #  time.sleep(10)
           # tempo_rimanente=tempo_rimanente-1
        #if tempo_rimanente==0:
         #   bot.sendMessage(chat_id,"live finita")
       
    elif msg['text'].startswith("/add"):
        thread1.add(int(msg["text"].replace("/add ","")))
        thread1.stampa_tempo()
        bot.sendMessage(chat_id,"aggiunti "+msg["text"].replace("/add ","")+" minuti")

    elif msg['text'].startswith("/stampa"):
        thread1.stampa_tempo()
        
    elif msg['text']=="/help":
        bot.sendMessage(chat_id,"utilizza /set X per impostare il tempo es.( /set 10 per 10 minuti ) /add X per aumentare il tempo /stop per fermare e /stampa per stampare i minuti rimanenti")

    elif msg['text']=="/stop":
        thread1.stop()
       
    else:
       bot.sendMessage(chat_id,"usa il comando /help per saperne di più")
       
TOKEN = '1464755124:AAHy7iBxhKWyXD1bUmCR3ZVVgESBae_9ies'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

while 1:
    time.sleep(1)

   
