
import requests


bot_message = ""
message = "start"

post_url = 'https://180f-110-39-9-132.in.ngrok.io/webhooks/rest/webhook'

r = requests.post(post_url, json={"message": message})
print("You -> ", message)
print("Bot -> ",end=' ')
for i in r.json():
    if 'text' in i:
        bot_message = i['text']
    print(f"{bot_message}")

while bot_message not in [
                          'Congratulations You rock!!!',
                          'Congratulations',
                          'Congrats You rock',
                          'Congrats']:

    message = input("You ->  ")
    if len(message)==0:
        continue
    # print("Sending message now...")

    r = requests.post(post_url, json={"message": message})

    print("Bot -> ",end=' ')

    bot_message = ''
    for i in r.json():
        if 'text' in i:
            bot_message = i['text']
        print(f"{bot_message}")
    
    if len(bot_message)==0:
        continue