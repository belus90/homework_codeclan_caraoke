import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Mr Bright Side", "American Rock", 2003)

    def test_song_name(self):
        self.assertEqual("Mr Bright", self.song.name)
    
    def test_song_type(self):
        self.assertEqual("Rock", self.song.type)
    
    def test_maden_year(self):
        self.assertEqual(1980, self.song.year)
    
    