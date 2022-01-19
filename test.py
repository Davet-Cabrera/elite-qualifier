import unittest
from main import good_or_bad

class TestGoodOrBad(unittest.TestCase):

    def test_good_or_bad(self):
      self.assertEqual(good_or_bad("okay","good","bad"), "good") 
      
      self.assertEqual(good_or_bad("not good","good","bad"), "bad")

if __name__ == '__main__':
    unittest.main()