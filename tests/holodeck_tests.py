import unittest

from classes.crewmember import *
from classes.holodeck import *

class TestHolodeck(unittest.TestCase):

    def setUp(self):
        self.holodeck_1 = (30,"Bride of Chaotica", "Flodder's Adventures")
        self.holodeck_2 = (60,"Fair Haven")
        self.holodeck_3 = (180, "Sherlock Holmes")
        self.holodeck_4 = (70, "Photons Be Free")
    
