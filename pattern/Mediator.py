import threading
import json
from message.Message import Item, Message

class Mediator:
    _instance_lock = threading.Lock()
    door : object
    detector : object
    wsClient : object
    window : object

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Mediator, "_instance"):
            with Mediator._instance_lock:
                if not hasattr(Mediator, "_instance"):
                    Mediator._instance = object.__new__(cls)
        return Mediator._instance

    def setDoor(self, door):
        self.door = door

    def setDetector(self, detector):
        self.detector = detector

    def setWSClient(self, wsClient):
        self.wsClient = wsClient


    def detect(self):
        self.detector.detect()

    
    def settleup(self):
        dif_count = self.detector.detect_difference()
        items = []
        for name, count in dif_count.items():
            item = Item(name, count)
            items.append(item)
        message = Message("settleup", items)
        self.wsSend(json.dumps(message, default=lambda x: x.__dict__))
        self.closeTheDoor()


    def openTheDoor(self):
        self.door.open()


    def closeTheDoor(self):
        self.door.close()


    def wsSend(self, msg : str):
        self.wsClient.send(msg)