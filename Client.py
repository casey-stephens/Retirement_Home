
class Client():

    def __init__(self):
        self.age = None
        self.room = None
        self.first_name = None
        self.last_name = None

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

    def setFirstName(self,f_name):
        self.first_name = f_name

    def getFirstName(self):
        return self.first_name

    def setLastName(self,l_name):
        self.last_name = l_name

    def getLastName(self):
        return self.last_name