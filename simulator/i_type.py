from simulator.py import registers
'''
[31:20] = imm[11:0]
[19:15] = rs1
[14:12] = funct3
[11:7] = rd
[6:0] = opcode
'''

# Function to sign-extend immediate value
def sext(imm):
    sign_bit = imm[0]
    return sign_bit*20 + imm[0:12] #sign-extend with sign bit


def i_type(asm_ins,registers,pc,mem):


    imm = asm_ins[20:32]
    rs1 = asm_ins[15:20]
    funct3 = asm_ins[12:15]
    rd = asm_ins[7:12]
    opcode = asm_ins[0:7]


    if funct3 == "000" and opcode == "0010011": #addi
        registers[rd] = (int(sext(imm),2) + registers[rs1])&0xFFFFFFFF


    elif funct3 == "011" and opcode == "0010011": #sltiu
        if registers[rs1] < int(sext(imm),2): # if unsigned(rs) < unsigned(imm)
            registers[rd] = 1 &0xFFFFFFFF
        else:
            registers[rd] = 0 &0xFFFFFFFF


    elif funct3 == "010" and opcode == "0000011": #lw
        base_reg = registers[rs1]
        imm_offset = int(sext(imm),2)

        fin_mem_addr = base_reg + imm_offset
        registers[rd] = mem[fin_mem_addr] &0xFFFFFFFF

        
    


