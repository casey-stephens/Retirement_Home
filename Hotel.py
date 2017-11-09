from FloorNode import *
from Client import *

class Hotel():
    def __init__(self):
        self.floor_Header = None
        self.dimensions = None

    def getFloorHeader(self):
        return self.floor_Header

    def getDimensions(self):
        return self.dimensions

    def setFloorHeader(self,floor_node):
        if isinstance(floor_node,FloorNode):
            self.floor_Header = floor_node
        else:
            print("must be a floornode to apply")

    def setDimensions(self,x,y):
        if isinstance(x,int) and isinstance(y,int):
            self.dimensions = (x,y)