#!/usr/bin/python

import immlib

DESC = "Play with Processes!"

def main(args):
    imm = immlib.Debugger()

    #imm.openProcess("C:\Documents and Settings\Administrator\Desktop\Server-Strcpy.exe")
    #imm.Attach(int(args[0]))

    moduleList = imm.getAllModules()
    td = imm.createTable("Module Information", ['Name', 'Base', 'Entry', 'Size', 'Version'])

    for entity in moduleList.values():
        td.add(0, [ entity.getName(),
                    '%08X' % entity.getBaseAddress(),
                    '%08X' % entity.getEntry(),
                    '%08X' % entity.getSize(),
                    entity.getVersion() ])

    imm.log(str(imm.getRegs()))
    
    return "Success"
