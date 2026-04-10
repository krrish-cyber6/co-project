# Function to sign-extend immediate value
def sext(imm):
    sign_bit = imm[0]
    return sign_bit*(32-len(imm)) + imm #sign-extend with sign bit


def ibin_op(asm_ins,registers,pc,mem):


    imm = asm_ins[0:12]
    rs1 = asm_ins[12:17]
    funct3 = asm_ins[17:20]
    rd = asm_ins[20:25]
    opcode = asm_ins[25:32]


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

    elif funct3 == "000" and opcode == "1100111": #jalr
        registers[rd] = pc + 4 #return address

        jump_to = registers[rs1] + int(sext(imm), 2) 

        # making LSB=0 before jumping
        bin_jump = format(jump_to,"032b")
        bin_jump = bin_jump[0:31] + "0"
        
        pc_jump = int(bin_jump,2) 

        return pc_jump

    return pc+4



        
    


