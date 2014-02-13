#class MyString :
#    def __init__(self, inputStr) :
#        string = inputStr
#        length = len(inputStr)

def IsPalindrome(n) :
    if n == n[::-1] :   # palindrome found
        return True
    else :
        return False

if __name__=="__main__" :
    import sys
    import os
    import getopt

    class Usage(Exception) :
        def __init__(self, msg) :
            self.msg = msg

    def main (argv = None) :
        if argv is None :
            argv = sys.argv
        try :
            try :
                opts, args = getopt.getopt(argv[1: ], "h", ["help"])
            except getopt.error, msg :
                raise Usage(msg)
            path = raw_input("Please enter in a path and filename >")
            input = []
            if not os.path.exists(path) :
                raise IOError, 'Invalid path or filename.'
            with open(path) as openFile :
                for line in openFile :
                    line = line.strip()
                    line = ''.join(line.split())
                    input.extend(line.rstrip('\r\n') )
            input = [ea.upper() for ea in input]
            print input
            longestString = ''

            input = 'aba'
            result = IsPalindrome(input)
            if result is True :
                print input, "is a Palindrome."
            else :
                print input, "is not a Palindrome."
        except Usage, err :
            print >> sys.stderr, err.msg
            print >> sys.stderr, "for help use --help"
            return 2

    if __name__=='__main__' :
        sys.exit(main())