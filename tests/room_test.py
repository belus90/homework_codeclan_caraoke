import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room= Room("90's room")
        self.song = Song("Mr Bright Side", "American Rock")
        self.new_guest = Guest("Antal Richard", 24, 15.6)

    def test_room_has_a_name(self):
        self.assertEqual("90's room", self.room.name)
    
    def test_the_room_is_empty(self):
        self.assertEqual(0, len(self.room.guests))
    
    def test_check_in_to_the_room(self):
        checking_guest = self.new_guest
        self.room.checking_in(checking_guest)
        expected = self.new_guest
        actual = self.room.guests[0]
        self.assertEqual(expected,actual)
    
    def test_check_out_of_the_room(self):
        guest = Guest("Vivien Nemeth", 27,58)
        self.room.checking_in(guest)
        self.room.checking_out(guest)
        self.assertEqual(0, self.room.guest_count())
    

    

