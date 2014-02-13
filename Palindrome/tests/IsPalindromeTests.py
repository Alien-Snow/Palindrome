import unittest
from Palindrome import MyString

class Test_IsPalindromeTests(unittest.TestCase):
    def testPalindromeFalse(self) :
        mine = MyString('aab')
        self.assertFalse(mine.IsPalindrome())

    def testPalindromeTrue(self) :
        mine = MyString('aba')
        self.assertTrue(mine.IsPalindrome())

    def test_single_letter_Palindrome(self) :
        mine = MyString('a')
        self.assertTrue(mine.IsPalindrome())

if __name__ == '__main__':
    unittest.main()
