import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Mr Bright Side", "American Rock")

    def test_song_name(self):
        self.assertEqual("Mr Bright Side", self.song.name)
    
    def test_song_type(self):
        self.assertEqual("American Rock", self.song.type)
    

    
