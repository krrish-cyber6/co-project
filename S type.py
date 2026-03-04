REGISTER_MAPPING = {
    "zero": "00000",  
    "ra":   "00001",  
    "sp":   "00010",  
    "gp":   "00011",
    "tp":   "00100",  
    "t0":   "00101",  
    "t1":   "00110", 
    "t2":   "00111", 
    "s0":   "01000",
    "s1":   "01001",
    "a0":   "01010", 
    "a1":   "01011", 
    "a2":   "01100", 
    "a3":   "01101", 
    "a4":   "01110", 
    "a5":   "01111",
    "a6":   "10000",
    "a7":   "10001",
    "s2":   "10010",
    "s3":   "10011",
    "s4":   "10100",
    "s5":   "10101",
    "s6":   "10110",
    "s7":   "10111",
    "s8":   "11000",
    "s9":   "11001",
    "s10":  "11010",
    "s11":  "11011",
    "t3":   "11100", 
    "t4":   "11101", 
    "t5":   "11110", 
    "t6":   "11111", 
}
s_type_info={"sw":{"funct3":"010","opcode":"0100011"}}

def s_type(instruction):    

    #parsing 
    part1=instruction.split()
    part2=part1[1].split(",")
    rs2=part2[0]
    base_offset=part2[1].strip(")").split("(")
    rs1=base_offset[1]
    imm=base_offset[0]
    
    #checking if the register is valid
    if rs1 not in REGISTER_MAPPING or rs2 not in REGISTER_MAPPING:
        print("invalid register")
        return
    
    #checking if immediate is an integer 
    try:
        int_imm=int(imm)
    except:
        print("immediate is not a valid integer")
        return
    
    #checking if the immediate is in the 12 bit 2's complement range 
    if not (-2048<=int_imm<=2047):
        print("the immediate can't be represented using a 12 bit 2's complement representation")
        return
    
    



