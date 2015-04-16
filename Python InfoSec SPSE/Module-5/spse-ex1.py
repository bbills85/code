#!/usr/bin/python

import immlib
import csv

DESC = "Write Process Data to a CSV File"

def main(args):

    imm = immlib.Debugger()
    
    csvFile = csv.writer(open("C:\Program Files\Immunity Inc\Immunity Debugger\PyCommands\ps.csv", "wb"))
    csvFile.writerow(['PID', 'Process', 'Path', 'Services'])
    
    psList = imm.ps()

    for process in psList:
        csvFile.writerow([str(process[0]), process[1], process[2], str(process[3])])
                                                               
    return "[+] Script Completed - C:\Program Files\Immunity Inc\Immunity Debugger\PyCommands\ps.csv"
