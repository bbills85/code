#!/usr/bin/python

import os,sys
import glob

def scanDirRecursively(dirToScan,level):
        for item in os.listdir(dirToScan):
                if os.path.isfile(os.path.join(dirToScan,item)):
                        print "----" * level + os.path.join(dirToScan,item)
                elif os.path.isdir(os.path.join(dirToScan,item)):
                        print "----" * level + os.path.join(dirToScan,item)
                        depth = level + 1
                        scanDirRecursively(os.path.join(dirToScan,item), depth)

# Will eunmerate all subdirs... use on root dir at your peril!
scanDirRecursively(sys.argv[1],0)

