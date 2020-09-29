class Item:
    def __init__(self, id, num):
        self.id = id
        self.num = num

class Message:
    def __init__(self, instruction, items):
        self.instruction = instruction
        self.items = items