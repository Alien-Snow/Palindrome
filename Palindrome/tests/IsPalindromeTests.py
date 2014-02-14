import unittest
from Palindrome import MyString

class Test_IsPalindromeTests(unittest.TestCase):
    def testPalindromeFalse(self) :
        slice = 'aab'
        self.assertFalse(MyString.IsPalindrome(slice))

    def testPalindromeTrue(self) :
        slice = 'aba'
        self.assertTrue(MyString.IsPalindrome(slice))

    def test_single_letter_Palindrome(self) :
        slice = 'a'
        self.assertTrue(MyString.IsPalindrome(slice))

if __name__ == '__main__':
    unittest.main()
