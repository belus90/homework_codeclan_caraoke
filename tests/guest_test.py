import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.new_guest = Guest("Antal Richard", 24, 15.6)

    def test_guest_has_a_name(self):
        self.assertEqual("Antal Richard", self.new_guest.name)
    
    def test_guest_has_some_money(self):
        self.assertEqual(15.6, self.new_guest.wallet)
    
    def test_guest_haas_an_age(self):
        self.assertEqual(24, self.new_guest.age)
    
