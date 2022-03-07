import unittest

from classes.crewmember import *
from classes.holodeck import *

class TestHolodeck(unittest.TestCase):

    def setUp(self):
        self.holodeck_1 = Holodeck(30,"Bride of Chaotica")
        self.holodeck_2 = Holodeck(60,"Fair Haven")
        self.holodeck_3 = Holodeck(180, "Sherlock Holmes")
        self.holodeck_4 = Holodeck(70, "Photons Be Free")
        self.holodeck_5 = Holodeck(45, "Flodder's Adventures")
    
    def test_holodeck_has_duration(self):
        self.assertEqual(30, self.holodeck_1.duration)

    def test_has_story(self):
        self.assertEqual("Sherlock Holmes", self.holodeck_3.story)