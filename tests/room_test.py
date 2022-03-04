import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_example = Room("90's room")
        self.song = Song("Mr Bright Side", "American Rock", 2003)
        self.new_guest = Guest("Antal Richard", 24, 15.6)

    def test_room_has_a_name(self):
        self.assertEqual("90's room", self.room_example.name)
    

