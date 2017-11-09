from Client import *
from FloorNode import *

class RoomNode():
    def __init__(self):
        self.right = None
        self.left = None
        self.room = None
        self.floor = None
        self.occupant = None
        self.is_head = False

    def setRight(self,rightNode):
        if isinstance(rightNode,RoomNode) or isinstance(rightNode,FloorNode):
            self.right = rightNode
        else:
            print("Must be a room node to add to Floor List")

    def setLeft(self,leftNode):
        if isinstance(leftNode,RoomNode) or isinstance(leftNode,FloorNode):
            self.left = leftNode
        else:
            print("Must be a room node to add to Floor List")

    def setRoom(self,newRoom):
        self.room = newRoom

    def setFloor(self,newFloor):
        self.floor = newFloor

    def setoccupant(self,newClient):
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

    def getIsHead(self):
        return self.is_head

    def setIsHead(self,value):
        if isinstance(value,bool):
            self.is_head = value
