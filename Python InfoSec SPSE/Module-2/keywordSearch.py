#! /usr/bin/python

import optparse

def readLog(logFile, keyword):
    """function that searches the specified file for the specific keyword,
    regardless of the case"""
    # try open the file in read mode
    try:
        inFile = open(logFile)

    # provide an error message if the file does not exisit
    except IOError:
        print "[-] Error could not locate the file '%s'" % logFile 

    # or procede with the search
    else:
        print "[+] searching '%s' for '%s'..." % (logFile, keyword)

        # for loop checking each line in the file
        for line in inFile.readlines():
            # if the keyword is in the file print the line and strip
            # the extra newline
            if keyword.lower() in line or keyword.upper() in line:
                print line.strip()

        # close the file
        inFile.close()
        print "[+] search complete..."


def main():
    """function used to parse and error check the input"""
    # setup usage prompt when user errors input
    parser = optparse.OptionParser('%prog ' + '-f <file> -k <keyword>')
    # add help information and dest name/type
    parser.add_option('-f', dest = 'filePath', type = 'string',\
        help = 'specify the file path to search through')
    # add help information and dest name/type
    parser.add_option('-k', dest = 'keyword', type = 'string',\
        help = 'specify the keyword to look for')

    # unpack args into tuple - options is a dict and args is a list
    (options, args) = parser.parse_args()
    # assign options to variables
    logFile = options.filePath
    keyword = options.keyword

    # error check, display help, and exit the program
    if logFile == None or keyword == None:
        parser.print_help()
        exit(0)

    # call readLog
    readLog(logFile, keyword)

if __name__ == '__main__':
    main()
