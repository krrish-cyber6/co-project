def sext(imm):
    sign_bit = imm[0]
    return sign_bit*(32-len(imm)) + imm #sign-extend with sign bit

def j_type(asm_ins,registers,pc,mem):
    '''
    The imm value is split across [20|10:1|11|19:12] so just collected them
    asm_ins[0] corresponds to bit 31 in imm[31:12]
    '''

    imm = asm_ins[0] + asm_ins[1:11] + asm_ins[11] + asm_ins[12:20] #!! CHECK THIS PART !!
    
    rd = asm_ins[7:12]
    opcode = asm_ins[0:7]


    if opcode == "1101111": #jal
        registers[rd] = pc + 4 # return address in rd
        jump_to = pc + int(sext(imm),2) # computing pc + offset to update the pc

        # making LSB=0 before jumping
        bin_jump = format(jump_to,"032b") #making jump_to binary 32bit
        bin_jump = bin_jump[0:31] + "0" #taking the first 31 chars(index 0 to 30) and then adding a 0 char at end to make lsb = 0
        
        pc_jump = int(bin_jump,2)  # convert to int and store in final pc_jump

        return pc_jump