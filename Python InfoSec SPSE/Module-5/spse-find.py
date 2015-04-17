#!/usr/bin/python

import immlib

DESC = "Find Instruction Address"

def main(args):
    imm = immlib.Debugger()

    assembleInstruction = imm.assemble(' '.join(args))
    
    if not assembleInstruction:
            return "[-] No Instruction Given"

    addressList = imm.search(assembleInstruction)
    
    table = imm.createTable("Instruction Location", ['Module', 'Base', 'Instruction Address', 'Instruction', 'Page Access'])

    for address in addressList:
        module = imm.findModule(address)

        if not module:
            imm.log("Module at address: 0x%08X does not exist" % address)
            continue
  
        instruction = ''
        numArgs = len(' '.join(args).split('\n'))
        
        for line in range(0, numArgs):
            instruction += imm.disasmForward(address, nlines = line).getDisasm() + ' '
            
        page = imm.getMemoryPageByAddress(address)
        pageAccess = page.getAccess(human = True)
        
        table.add(0,
                    [module[0],
                    str("0x%08X" % module[1]),
                    str("0x%08X" % address),
                    instruction,
                    pageAccess])

    return "Success"
