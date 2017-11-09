from FloorNode import *
from RoomNode import *

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

    def Search(self,user_input):
        None

    def Insert(self,user_input):
        args = user_input.strip().split(":")
        if int(args[0])>self.dimensions[0] or int(args[1])>self.dimensions[1]:
            print("Room not within dimensions ("+str(self.dimensions[0]) +"," +str(self.dimensions[1]) + ")")
            return
        room_number = int(args[1])
        floor_number = int(args[0])
        floor_traverser = self.floor_Header

        for i in range(0,floor_number): #0 represents the head node
            floor_traverser = floor_traverser.getUp()
            print("current floor :" + str(floor_traverser.getFloor()) + "current counter =" + str(i))
            i += 1


        room_traverser = floor_traverser.getRoomHeader()

        for i in range(0,room_number):
            room_traverser = room_traverser.getRight()
            i +=1

        print(str(room_traverser.floor) +":" + str(room_traverser.room) )
        room_string = str(room_traverser.floor) +":" + str(room_traverser.room)
        new_client = Client()
        new_client.setFirstName(input("Input Clients First Name: "))
        new_client.setLastName(input("Input Clients Last Name: "))
        new_client.setAge(int(input("Input Clients Age: ")))
        new_client.setRoom(room_string)

        room_traverser.setOccupant(new_client)
        print(new_client.getFirstName()+" has been registered for room " + room_string)
        return


    def Delete(self,user_input):
        None

    def Traverse(self):
        None

    def Vacancies(self):
        None

    def List(self):

        floor_traverser = self.floor_Header
        floor_traverser = floor_traverser.getDown()         #start with top floor

        while floor_traverser.getFloor() != 0:
            room_head = floor_traverser.getRoomHeader()
            room_traverser = room_head.getRight()
            print("floor traverser value = " + str(floor_traverser.getFloor()))
            print("room traverser value = " + str(room_traverser.getRoom()))
            while room_traverser != room_head:
                client = room_traverser.getOccupant()
                name = ""
                if client.getFirstName() == None:
                    name = "N/A"
                else:
                    name = client.getFirstName()+" "+client.getLastName()
                room_string = "[" + str(floor_traverser.getFloor()) + ":" + str(room_traverser.getRoom()) + ":" + str(name) + "] - "
                print(room_string, end="")
                room_traverser = room_traverser.getRight()
            floor_traverser = floor_traverser.getDown()
        return



    def Save(self):
        None

