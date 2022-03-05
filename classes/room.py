class Room:
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs =[]

    def checking_in(self, guest):
        self.guests.append(guest)

    def checking_out(self, guest_to_check_out):
        self.guests.remove(guest_to_check_out)
    
    def guest_count(self):
        return len(self.guests)
    
        