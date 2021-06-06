class Hotel:
    def __init__(self, rooms, floors, Room):
        self.rooms = rooms
        self.floors = floors

        rooms_per_floor = int(self.rooms/self.floors)
        last_floor_rooms = self.rooms % self.floors

        room_numbers = [int(room) for room in range(1, self.rooms+1)]

        self.rooms_list = []
        self.building = []
        for floor in range(self.floors):
            floors_here = []
            for room in range(0, rooms_per_floor):
                # floors_here.append(room_numbers.pop(0))
                self.rooms_list.append(Room(room_numbers.pop(0), floor))
            self.building.append(floors_here)

        last_floor = []
        for floor in range(0, last_floor_rooms):
            self.rooms_list.append(Room(room_numbers.pop(0), self.floors-1))
        self.building[len(self.building)-1].extend(last_floor)

    def get_rooms_list(self):
        return self.rooms_list


class Room:
    def __init__(self, room_nr, floor):
        self.room_nr = room_nr
        self.floor = floor
        self.guest = 0

        print("nr:", self.room_nr, "piętro:", self.floor, "gość:", self.guest)

    def show_rooms(self):

        if self.guest == 0:
            to_print = "-----"
        else:
            to_print = str(self.guest)

        print("nr:", self.room_nr, "piętro:", self.floor, "gość:", to_print)

    def leave_room(self):
        self.guest = 0
        print("Pokój został zwolniony")


class Person(Hotel):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def take_room(self, room, room_nr):
        self.room_nr = room_nr

        if room.guest == 0:
            room.guest = self.name
            print(self.name, "wynajął pokój", self.room_nr+1)
        else:
            print(self.name, "ten pokój jest zajęty")


floors = int(input("piętra: "))
rooms = int(input("pokoje: "))
if floors > rooms:
    print("Nie może być mniej niż jeden pokój na piętro!")
    exit()
else:
    h = Hotel(rooms, floors, Room)
    room_list = Hotel.get_rooms_list(h)
    guest_list = []
    while True:
        print("<1> Dodaj gościa")
        print("<2> Zajmij pokój")
        print("<3> Zwolnij pokój")
        choice = int(input("wybierz: "))
        if choice == 1:
            name = input("Podaj nazwę gościa: ")
            guest_list.append(Person(name))
        elif choice == 2:
            i = 1
            for name in guest_list:
                print(i, name)
                i += 1
            guest = int(input("Komu chcesz wynająć pokój (id): "))
            for room in room_list:
                room.show_rooms()
            room_to_give = int(input(f"Który pokój ma wziąć: "))-1
            guest_list[guest -
                       1].take_room(room_list[room_to_give], room_to_give)
        elif choice == 3:
            for room in room_list:
                room.show_rooms()
            room_to_leave = int(input("Który pokój chcesz zwolnić: "))
            room_list[room_to_leave-1].leave_room()
