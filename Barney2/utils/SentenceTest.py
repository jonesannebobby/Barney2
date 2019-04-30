
import unittest
from utils.Sentence import Sentence
from utils.Direction import Direction

class TestSentence(unittest.TestCase):

    def setUp(self):
        self.sentence = Sentence(Direction.OUT,"Check These Sentence")

    def test_uppercase(self):
        self.assertTrue(self.sentence.containsPhrase("THESE"))
        
    def test_lowercase(self):
        self.assertTrue(self.sentence.containsPhrase("these"))

    def test_mixedcase(self):
        self.assertTrue(self.sentence.containsPhrase("These"))

    def test_nomatch(self):
        self.assertFalse(self.sentence.containsPhrase("That"))

    def test_nomatch_part_word(self):
        self.assertFalse(self.sentence.containsPhrase("The"))

    def test_two_words(self):
        self.assertTrue(self.sentence.containsPhrase("Check These"))
        

