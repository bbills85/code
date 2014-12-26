#!/usr/bin/python

import os
import optparse

def listDir(path):
    """function that lists all directories and files recursively"""
    # for loop, stores dirpath, dirnames, and filenames in a tuple
    for (dirpath, dirnames, filenames) in os.walk(path):
        # set depth to the amount of directoies it takes
        # to get to the current directory
        depth = len(dirpath.split('/'))
        # print directory name
        print depth * '-' + '[ ' + dirpath.split('/')[-1] + ' ]'
        # for loop to print all files located in a directory
        for files in filenames:
            print depth * '--' + files

def main():
    """function used to parse and error check user input"""
    # setup usage prompt when user errors input
    parser = optparse.OptionParser('%prog ' + '-p <path>')
    # add help information and dest name/type
    parser.add_option('-p', dest = 'path', type = 'string',\
        help = 'specify the path to traverse')

    # unpack args into tuple - options is a dict and args is a list
    (options, args) = parser.parse_args()
    # assign options to variables
    path = options.path

    # error check, display help, and exit the program
    if path == None:
        parser.print_help()
        exit(0)
    # calls function listDir
    listDir(path)

if __name__ == '__main__':
    main()
