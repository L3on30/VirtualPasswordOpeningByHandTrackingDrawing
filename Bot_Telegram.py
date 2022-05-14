import telegram
import cv2
import os
def bot_message():

    try:
        #Use this token to access the HTTP API:
        notify = telegram.Bot("abc")
        #Read file 
        f1 = open("PassLog/Log.txt", 'r+', encoding='UTF-8')
        data1 = f1.read()
        message1 = "{}".format(data1)
        notify.send_message(chat_id="123", text=message1, parse_mode='Markdown')
    except Exception as ex:
        print(ex)
        
def bot_photo():
    try:
        notify = telegram.Bot("abc")
        notify.send_photo(chat_id="123", photo = open('Fail/Human.png', 'rb'), caption = "?")
    except Exception as ex:
        print(ex)
