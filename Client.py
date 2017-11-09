
class Client():

    def __init__(self):
        self.age = None
        self.room = None

    def setAge(self,newage):
        if isinstance(newage,int):
            self.age = newage
        else:
            print("Age must be integer")

    def setRoom(self,newroom):
        self.room = newroom

    def getAge(self):
        return self.age

    def getRoom(self):
        return self.room