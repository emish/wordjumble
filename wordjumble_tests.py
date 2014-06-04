import unittest
from wordjumble import *

class TestContains(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(contains("", ""))
        
    def test_spaces(self):
        self.assertTrue(contains(" ", " "))
        self.assertTrue(contains("", " "))

    def test_basic(self):
        self.assertTrue(contains('a', 'ab'))
        self.assertTrue(contains('abc', 'abcd'))

    def test_interleaving(self):
        self.assertTrue(contains('bgx', 'abcdefghijkxyz'))

    def test_not_contains(self):
        self.assertFalse(contains('abc', 'foobar'))
        self.assertFalse(contains('bgu', 'abgxyz'))

    def test_duplicate_contains_false(self):
        self.assertFalse(contains('aa', 'abcd'))
        self.assertFalse(contains('abbcc', 'abbbbc'))

    def test_duplicate_contains_true(self):
        self.assertTrue(contains('aa', 'aabcd'))
        self.assertTrue(contains('abbcc', 'aaaaaaaabbbbbccc'))

class TestValidWords(unittest.TestCase):
    def test_no_matches(self):
        self.assertFalse(find_valid_words('x'))
        self.assertFalse(find_valid_words('zzz'))


if __name__ == '__main__':
    unittest.main()

