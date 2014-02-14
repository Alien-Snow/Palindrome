#! /usr/bin/python

if __name__=="__main__" :
    import sys
    import os
    import getopt
    from Palindrome import MyString

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
            path = raw_input("Please enter in a path and filename >")   # start of input
            input = []
            if not os.path.exists(path) :
                raise IOError, 'Invalid path or filename.'
            with open(path) as openFile :
                for line in openFile :
                    line = line.strip()
                    line = ''.join(line.split())
                    input.extend(line.rstrip('\r\n') )
            input = [ea.upper() for ea in input]                        # input processed
            mine = MyString(input)
            idx = 0
            while idx < mine.length :
                mine.FindPalindrome(idx)
                idx += 1
            mine.PrintLongestFound()
        except Usage, err :
            print >> sys.stderr, err.msg
            print >> sys.stderr, "for help use --help"
            return 2

    if __name__=='__main__' :
        sys.exit(main())