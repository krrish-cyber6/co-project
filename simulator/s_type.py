def s_type(binary_instruction,registers,memory,pc):
    
    opcode=binary_instruction[25:]
    funct3=binary_instruction[17:20]  
    rs1=binary_instruction[12:17]
    rs2=binary_instruction[7:12]  
    immediate_binary=binary_instruction[:7] + binary_instruction[20:25]
    immediate_integer=int(immediate_binary,2)

    if opcode !="0100011":
        raise KeyError("Invalid opcode")
    
    if funct3 !="010":
        raise KeyError("Invalid funct3 for S-type")
    
    if immediate_binary[0]=="1":
        immediate_integer=immediate_integer-2**12
   
    address=registers[rs1]+immediate_integer
    memory[address]=registers[rs2]
    
    return pc + 4
    

