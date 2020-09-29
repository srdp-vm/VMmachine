from Detector import Detector
from Door import Door
from WSClient import WSClient
from pattern.Mediator import Mediator

if __name__ == '__main__':
    ws_client = WSClient(url="ws://192.168.1.100:8080/VM3.0/websocket/machine")
    detector = Detector()
    door = Door()
    Mediator().setDetector(detector)
    Mediator().setDoor(door)
    Mediator().setWSClient(ws_client)
    try:
        while input() != "exit":
            pass
    finally:
        door.clean()
        ws_client.close()
