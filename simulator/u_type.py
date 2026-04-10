def u_type(binary_instruction,registers,pc):
    immediate_binary=binary_instruction[0:20]
    rd=binary_instruction[20:25]
    opcode=binary_instruction[25:]   
    
    immediate_integer=int(immediate_binary,2)

    if immediate_binary[0]=="1":
        immediate_integer=immediate_integer-2**20

    immediate_integer=immediate_integer<<12

    if opcode=="0110111":
        registers[rd]=immediate_integer 
    
    elif opcode=="0010111":
        registers[rd]=pc+immediate_integer  

    else:
        raise KeyError("Invalid opcode for U-type")          
    
    return pc + 4
