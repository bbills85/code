#!/usr/bin/python

import immlib

DESC = "A Simple Hello World Script"

def main(args):

    imm = immlib.Debugger()
    
    imm.log("Writing to my Log Window")
    imm.updateLog()
    
    td = imm.createTable("SPSE Course", ["PID", "Name", "Path", "Services"])
    psList = imm.ps()

    for process in psList:
        td.add(0, [str(process[0]), process[1], process[2], str(process[3])])
                                                               
    return "[+] Hello to the World of ID Scripting!"
