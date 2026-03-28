def rbin_op(bin_instruction, registers):
    funct7 = bin_instruction[0:7]
    rs1 = [bin_instruction[7:12]]
    rs2 = bin_instruction[12:17]
    funct3 = bin_instruction[17:20]
    rd = bin_instruction[20:25]
    opcode = bin_instruction[25:]
    