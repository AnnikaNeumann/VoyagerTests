import unittest

from classes.crewmember import *
from classes.holodeck import *

class TestCrewmember(unittest.TestCase):

    def setUp(self):

        self.crewmember_1 = ("The Doctor", 2371, "EMH", "Chief Medical Officer", "Beowulf")
        self.crewmember_2 = ("Tom Paris", "Lieutenant", "Helmet", "Captain Proton")
        self.crewmember_3 = ("Kathryn Janeway", "Vice Admiral", "Captain", "Fair Haven")
        self.crewmember_4 = ("B'Elanna Torres", 2346, "Lieutenant", "Chief Engineer", "Photons Be Free")
    
# note : Date of Birth of Tom Paris and Kathryn Janeway unknown 

    def test_crewmember_has_name(self):
        self.assertEqual("Kathryn Janeway", self.crewmember_3.name)
