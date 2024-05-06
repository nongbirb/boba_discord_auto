from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
import json
import random

#Load Config
with open('./config.json') as f:
  data = json.load(f)
  for c in data['Config']:
        print('Loading...')
channelids = c['channelids']  
token = c['token'] #modify this in config.json
messages = c['messages']
header_data = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": token
} 
 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v7/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Message Sent") 
            pass 
 
        else: 
            stderr.write(f"HTTP {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
 
def main(): 
    random_channel_id = random.choice(channelids)  # Randomly select a channel ID
    message_data = {
        "content": random.choice(messages),  # Randomly select a message
        "tts": "false"
    }

    send_message(get_connection(), random_channel_id, dumps(message_data))
 
if __name__ == '__main__': 
	while True:    
		main()      
		sleep(random.randint(120, 150)) #How often the message will be sent (in seconds), every 1 hour = 3600
