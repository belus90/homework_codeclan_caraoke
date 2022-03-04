import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_example = Room("90's room")

    def test_room_has_a_name(self):
        self.assertEqual("70's song", self.room_example.name)
    
    # def test_room_is_empty(self):
    #     self.assertEqual(0, len())
