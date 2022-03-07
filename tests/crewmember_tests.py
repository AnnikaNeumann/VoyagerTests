import unittest

from classes.crewmember import *
from classes.holodeck import *

class TestCrewmember(unittest.TestCase):

    def setUp(self):

        self.crewmember_1 = Crewmember("The Doctor", 2371, "EMH", "Chief Medical Officer", "Beowulf")
        self.crewmember_2 = Crewmember("Tom Paris", 0,"Lieutenant", "Helmet", "Captain Proton")
        self.crewmember_3 = Crewmember("Kathryn Janeway", 0,"Vice Admiral", "Captain", "Fair Haven")
        self.crewmember_4 = Crewmember("B'Elanna Torres", 2346, "Lieutenant", "Chief Engineer", "Photons Be Free")
        
        # note : Date of Birth of Tom Paris and Kathryn Janeway unknown 


    def test_crewmember_has_name(self):
        self.assertEqual("B'Elanna Torres", self.crewmember_4.name)

    def test_crewmember_has_dob(self):
        self.assertEqual(2371, self.crewmember_1.dob)

    def test_crewmember_has_rank(self):
        self.assertEqual("Vice Admiral", self.crewmember_3.rank)

    def test_crewmember_has_story(self):
        self.assertEqual("Photons Be Free", self.crewmember_4.fav_holodeck_story)