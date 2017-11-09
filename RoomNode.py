from Client import *


class RoomNode():
    def __init__(self):
        self.right = RoomNode
        self.left = RoomNode
        self.room = None
        self.floor = None
        self.occupant = Client()
        self.isHead = bool

    def setRight(self,rightNode):
        if isinstance(rightNode,RoomNode):
            self.right = rightNode
        else:
            print("Must be a room node to add to Floor List")

    def setLeft(self,leftNode):
        if isinstance(leftNode,RoomNode):
            self.left = leftNode
        else:
            print("Must be a room node to add to Floor List")

    def setRoom(self,newRoom):
        self.room = newRoom

    def setFloor(self,newFloor):
        self.floor = newFloor

    def setOccupant(self,newClient):
        if isinstance(newClient,Client):
            self.occupant = newClient
        else:
            print("Must be a Client object to add to room node")

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getRoom(self):
        return self.room

    def getFloor(self):
        return self.floor

    def getOccupant(self):
        return self.occupant

    def setIsHead(self,arg):
        if isinstance(arg,bool):
            self.isHead = arg
        else:
            print("must be a boolean")

    def getIsHead(self):
        return self.isHead