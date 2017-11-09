from Hotel import *


active = True       #used to keep execution chain running, when false application exits
hotel = Hotel()     #data structure that holds both floor and room nodes in one place

def createNewSession():

    print("Creating New Session")
    correctness = False         #boolean used for user input loop
    while correctness != True:
        floor_input = input("How many Floors?").strip()
        room_input = input("How many Rooms per Floor?").strip()

        if floor_input.isdigit() and room_input.isdigit():
            correctness = True
            hotel.setDimensions(int(floor_input),int(room_input))
        else:
            print("Incorrect inputs, must be integers")

    floor_head_node = FloorNode()       #initialize the floorhead (create the elevator)
    floor_head_node.setIsHead(True)
    floor_head_node.setFloor(0)
    room_header = RoomNode()
    room_header.setRoom(0)
    room_header.setFloor(0)
    room_header.setIsHead(True)
    floor_head_node.setRoomHeader(room_header)

    hotel.setFloorHeader(floor_head_node)
    dimensions = hotel.getDimensions()
    traversal_node = floor_head_node

    print("Floor Node is Set: building Structure")

    for y in range(1,dimensions[0]+1):            #generating floors
        print("Adding Floor "+str(y))
        new_floor_node = FloorNode()
        new_floor_node.setFloor(y)
        if traversal_node == floor_head_node:           #First Node attachment to head
            print("Found Head Node For floor")
            traversal_node.setUp(new_floor_node)
            traversal_node = traversal_node.getUp()
        elif y == (dimensions[0]):                    #Final node attachment, loops back to head node
            new_floor_node.setDown(traversal_node)
            new_floor_node.setUp(floor_head_node)
            floor_head_node.setDown(new_floor_node)
            traversal_node.setUp(new_floor_node)
            print("Added Top Floor")
        else:                                           #normal node attachment
            new_floor_node.setDown(traversal_node)
            traversal_node.setUp(new_floor_node)
            traversal_node = traversal_node.getUp()
                                                         #setting room header information for the floor
        new_floor_room_header = RoomNode()
        new_floor_room_header.setIsHead(True)
        new_floor_room_header.setRoom(0)
        new_floor_room_header.setFloor(y)
        new_floor_node.setRoomHeader(new_floor_room_header)
        room_traversal = new_floor_node.getRoomHeader()

        for x in range(1,dimensions[1]+1):                #Adding rooms for each floor generated
            print("Adding Room " +str(x))
            new_room_node = RoomNode()
            new_room_node.setFloor(y)
            new_room_node.setRoom(x)
            if room_traversal == new_floor_room_header:    #First Node Attachment
                print("Found Head Node for Rooms on Floor "+str(y) + ". Attaching Room " + str(x) + " to head")
                room_traversal.setRight(new_room_node)
                room_traversal = room_traversal.getRight()
            elif x == (dimensions[1]):                            #Final Node attachment, loops back to head
                print("Adding Last Room ("+str(x)+") for Floor " + str(y))
                new_room_node.setLeft(room_traversal)
                new_room_node.setRight(new_floor_node.getRoomHeader())
                room_traversal.setRight(new_room_node)
            else:                                                   #Normal node attachment
                new_room_node.setLeft(room_traversal)
                room_traversal.setRight(new_room_node)
                room_traversal = new_room_node


    print("Floors and Rooms have been generated")


#execution chain starts here
current_input = None        #will be used for each prompt
print("Welcome to Sunnyvale Retirement's Database System")
current_input = input("Load previous session?")
correctness = False

while correctness != True:
    if current_input.strip() == "yes" or current_input.strip() == "y" or current_input.strip() == "Yes" or current_input.strip() == "YES" or current_input.strip() == "Y":
        None#loadPreviousSession()
        correctness = True
    elif current_input.strip() == "no" or  current_input.strip() == "n" or current_input.strip() == "NO" or current_input.strip() == "No" or current_input.strip() == "N":
        createNewSession()
        correctness = True
    else:
        print("Incorrect Input: try 'Yes' or 'No")

print("Basic Actions Include:")
print("1.Search: search for either an individuals name or a room number.")
print("2.Insert: used to insert a new individual into a room")
print("3.Delete: use a room number or name to remove an occupant")
#print("4.Traverse: allows user to traverse floors and rooms using directional keys")
print("5.Vacancies: lists all vacant rooms per floor")
print("6.List: Outputs a full list of all rooms and occupants")
print("7.Save: Outputs the changes made to the 'Saved Data' File")
print("8.Exit: exits the application")

while active:
    current_input = input("Input an Action:").strip()
    if current_input == "search" or current_input == "Search" or current_input == "1":
        current_input = input("Enter a name or roomnumber. If both First and last Name, please separate with a space \n If a roomnumber, use the following format Floor:Room (eg. 05:03 is the third room of floor 5): ")
        hotel.search(current_input)
    if current_input == "insert" or current_input == "Insert" or current_input == "2":
        current_input = input("Pick a room. Room format is as follows, Floor:Room (eg. 05:03 is the third room of floor 5)")
        hotel.Insert(current_input)
    if current_input == "delete" or current_input == "Delete" or current_input == "3":
        current_input = input("Enter a name or roomnumber. If both First and last Name, please separate with a space \n If a roomnumber, use the following format Floor:Room (eg. 05:03 is the third room of floor 5): ")
        hotel.Delete(current_input)
    if current_input == "traverse" or current_input == "Traverse" or current_input == "4":
        hotel.Traverse()
    if current_input == "vacancies" or current_input == "Vacancies" or current_input == "5":
        hotel.Vacancies()
    if current_input == "list" or current_input == "List" or current_input == "6":
        hotel.List()
    if current_input == "Save" or current_input == "save" or current_input == "7":
        hotel.Save()
    if current_input == "Exit" or current_input == "exit" or current_input == "8":
        active = False





