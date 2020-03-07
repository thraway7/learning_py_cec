import time, datetime

import RPi.GPIO as GPIO

import telepot

from telepot.loop import MessageLoop

led = 18

now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

 #LED

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, 0) #Off initially

def action(msg):

    chat_id = msg['chat']['id']

    command = msg['text']

    print ('Received: %s' % command)

    if 'on' in command:

        message = "Turned on "

        if 'led' in command:

            message = message + "led"

            GPIO.output(led, 1)

            telegram_bot.sendMessage (chat_id, message)

 

    if 'off' in command:

        message = "Turned off "

        if 'led' in command:

            message = message + "led "

            GPIO.output(led, 0)        

        telegram_bot.sendMessage (chat_id, message)

telegram_bot = telepot.Bot('921547197:AAFij23fW-asl2PYjMy08_RDiNCiUiTLJfk')

print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()

print ('Up and Running....')

while 1:

    time.sleep(10)
