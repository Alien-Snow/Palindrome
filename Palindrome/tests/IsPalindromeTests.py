import unittest
from Palindrome import IsPalindrome

class Test_IsPalindromeTests(unittest.TestCase):
    def testPalindromeFalse(self) :
        testStr = 'aab'
        self.assertFalse(IsPalindrome(testStr))

    def testPalindromeTrue(self) :
        testStr = 'aba'
        self.assertTrue(IsPalindrome(testStr))

    def test_single_letter_Palindrome(self) :
        testStr = 'a'
        self.assertTrue(IsPalindrome(testStr))

if __name__ == '__main__':
    unittest.main()
