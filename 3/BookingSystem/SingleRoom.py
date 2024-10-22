from Room import Room


class SingleRoom(Room):

    def __init__(self, room_number, price):
        super().__init__(room_number, price)
        self.extras = ["mini bar", "tv"]

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
        else:
            print("Hiba, a szoba már foglalt!")

    def unbook_room(self):
        if self.is_booked:
            self.is_booked = False
        else:
            print("Hiba, a szoba nem is volt foglalt!")