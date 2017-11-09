import RoomNode

class FloorNode():
    def __init__(self):
        self.up = None                          #up and down are each a floor node. if ground level, down will be null. vice versa for top level
        self.down = None
        self.room_header = None                 #each floor will have a room header to start the room linked list, think of it as the elevator exit, next room is the first on the floor
        self.floor_number = None
        self.is_head = False                  #used to indicate if the floor node is the header node, aka: ground floor

    def setUp(self,up_node):
        if isinstance(up_node,FloorNode):
            self.up = up_node
        else:
            print("Must be a floor node")

    def setDown(self,down_node):
        if isinstance(down_node,FloorNode):
            self.down = down_node
        else:
            print("Must be a floor node")

    def setFloor(self,new_floor):
        if isinstance(new_floor,int):
            self.floor_number = new_floor
        else:
            print("Floor number must be an integer")

    def setIsHead(self, is_ground):
        if isinstance(is_ground,bool):
            self.is_head = is_ground

    def getFloor(self):
        return self.floor_number

    def getUp(self):
        return self.up

    def getDown(self):
        return self.down

    def getRoomHeader(self):
        return self.room_header

    def setRoomHeader(self,new_room_node):
        if isinstance(new_room_node, RoomNode.RoomNode):
            self.room_header = new_room_node
        else:
            print("Room header must be a floor node")

    def getIsHead(self):
        return self.is_head

