import Jetson.GPIO as GPIO
import json
from pattern.Mediator import Mediator
from message.Message import Message
from message.Message import Item


class Door:
    def __init__(self):
        self.relay = 12
        self.sensor = 13
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sensor, GPIO.IN)
        GPIO.setup(self.relay, GPIO.OUT, initial=GPIO.LOW)
        GPIO.add_event_detect(self.sensor, GPIO.BOTH, callback = lambda x: self.onChange() , bouncetime = 50)

    
    def clean(self):
        GPIO.cleanup()

    
    def open(self):
        GPIO.output(self.relay, GPIO.HIGH)


    def close(self):
        GPIO.output(self.relay, GPIO.HIGH)

    def onChange(self):
        cur = GPIO.input(self.sensor)
        if cur == GPIO.HIGH:
            print("Current sensor value HIGH")
        elif cur == GPIO.LOW:
            # means door is closed, it's time to detect and calculate the diff
            print("Current sensor value LOW")
            Mediator().settleup()