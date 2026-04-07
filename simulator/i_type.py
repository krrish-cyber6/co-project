from simulator.py import registers
'''
[31:20] = imm[11:0]
[19:15] = rs1
[14:12] = funct3
[11:7] = rd
[6:0] = opcode
'''
def sext(imm):
    return imm[0]*20 + imm[0:12]

def i_type(asm_ins):
    b_imm = asm_ins[20:32]
    imm = int(asm_ins[20:32],2)
    rs1 = int(asm_ins[15:20],2)
    funct3 = asm_ins[12:15]
    rd = int(asm_ins[7:12],2)
    opcode = asm_ins[0:7]

    if funct3 == "000" and opcode == "0010011": #addi
        registers[rd] = format((int(sext(b_imm),2) + int(registers[rs1],2))&0xFFFFFFFF,"032b")


        
    


