from simulator.py import registers
'''
[31:20] = imm[11:0]
[19:15] = rs1
[14:12] = funct3
[11:7] = rd
[6:0] = opcode
'''
def sext(imm):
    

def sim_i(asm_ins):
    imm = int(asm_ins[20:32])
    rs1 = int(asm_ins[15:20])
    funct3 = asm_ins[12:15]
    rd = int(asm_ins[7:12])
    opcode = asm_ins[0:7]

    if funct3 == "000" and opcode == "0010011": #addi
        registers[rd] = format(imm + registers[rs1],"032b")


        
    


