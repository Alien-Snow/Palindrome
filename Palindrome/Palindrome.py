class MyString(object):

    def __init__(self, inputStr) :
        self.string = inputStr
        self.length = len(inputStr)
        self.longest = ''
        self.position = 0

    @staticmethod
    def IsPalindrome(slice) :
        if slice == slice[::-1] :   # palindrome found
            return True
        else :
            return False

    def PrintLongestFound(self) :
        line = ''
        if len(self.longest) < 2 :
            print '\n\nThe string :\n', line.join(self.string)
            print('Doesn\'t have a palindrome.\n')
        else :
            print '\n\nThe longest palindrome in :\n', line.join(self.string), '\nis\n', line.join(self.longest), '\n'

    def FindPalindrome(self, index, offset = 1) :
            if ((index + offset + 1) >= (self.length - 1)) | ((index - offset) < 0) :
                return
            elif self.IsPalindrome(self.string[index - offset : index + offset + 1]) :
                self.Compare(self.string[index - offset : index + offset + 1])
                offset += 1
                self.FindPalindrome(index, offset)
            else :
                return

    def Compare(self, found) :
        if len(found) > len(self.longest) :
            self.longest = found
        else :
            return