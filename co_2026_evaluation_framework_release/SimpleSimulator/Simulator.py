import sys

registers = {
    "00000": 0x00000000,
    "00001": 0x00000000,
    "00010": 0x0000017C,  
    "00011": 0x00000000,
    "00100": 0x00000000,
    "00101": 0x00000000,
    "00110": 0x00000000,
    "00111": 0x00000000,
    "01000": 0x00000000,
    "01001": 0x00000000,
    "01010": 0x00000000,
    "01011": 0x00000000,
    "01100": 0x00000000,
    "01101": 0x00000000,
    "01110": 0x00000000,
    "01111": 0x00000000,
    "10000": 0x00000000,
    "10001": 0x00000000,
    "10010": 0x00000000,
    "10011": 0x00000000,
    "10100": 0x00000000,
    "10101": 0x00000000,
    "10110": 0x00000000,
    "10111": 0x00000000,
    "11000": 0x00000000,
    "11001": 0x00000000,
    "11010": 0x00000000,
    "11011": 0x00000000,
    "11100": 0x00000000,
    "11101": 0x00000000,
    "11110": 0x00000000,
    "11111": 0x00000000
}


memory = []
for i in range(0,32):
    memory.append(0&0xFFFFFFFF)

#r-type part
def sext(imm):
    sign_bit = imm[0]
    return sign_bit*(32-len(imm)) + imm #sign-extend with sign bit

def signed(n,n1):
    temp=format(n,f"0{n1}b")
    if temp[0]=="1":
        return n-2**n1
    else:
        return n

def rbin_op(bin_instruction, registers,pc):
    funct7 = bin_instruction[0:7]
    rs2 = bin_instruction[7:12]
    rs1 = bin_instruction[12:17]
    funct3 = bin_instruction[17:20]
    rd = bin_instruction[20:25]
    opcode = bin_instruction[25:]
    if funct7=="0100000" and funct3!="000":
        raise KeyError
    elif funct7=="0100000":
        registers[rd]=(registers[rs1]-registers[rs2])&0xFFFFFFFF
    elif funct7=="0000000":
        if funct3=="000":
            registers[rd]=(registers[rs1]+registers[rs2])&0xFFFFFFFF
        elif funct3=="001":
            registers[rd]=((registers[rs1]&0xFFFFFFFF)<<(registers[rs2]&31))&0xFFFFFFFF
        elif funct3=="010":
            registers[rd]=(int(signed(registers[rs1],32)<signed(registers[rs2],32)))&0xFFFFFFFF
        elif funct3=="011":
            registers[rd]=int((registers[rs1])<(registers[rs2]))&0xFFFFFFFF
        elif funct3=="100":
            registers[rd]=(registers[rs1]^registers[rs2])&0xFFFFFFFF
        elif funct3=="101":
            registers[rd]=((registers[rs1]&0xFFFFFFFF)>>(registers[rs2]&31))&0xFFFFFFFF
        elif funct3=="110":
            registers[rd]=(registers[rs1]|registers[rs2])&0xFFFFFFFF
        elif funct3=="111":
            registers[rd]=(registers[rs1]&registers[rs2])&0xFFFFFFFF
        else :
            return pc+4
            raise KeyError
        
    return pc+4
        
def bbin_op(ins,pc,registers):
    opcode=ins[25:]
    func3=ins[17:20]
    r1=registers[ins[12:17]]
    r2=registers[ins[7:12]]
    imm=ins[0]+ins[24]+ins[1:7]+ins[20:24]+"0"
    offset=int(imm,2)
    if offset & 1<<12:
        offset-=1<<13

    if func3=="000":
        if r1==r2:
            pc+=offset
        else:
            pc+=4
    elif func3=="001":
        if r1!=r2:
            pc+=offset
        else:
            pc+=4
    elif func3=="100":
        if r1<r2:
            pc+=offset
        else:
            pc+=4
    elif func3=="101":
        if r1>=r2:
            pc+=offset
        else:
            pc+=4
    elif func3=="110":
        if (r1 & 0xFFFFFFFF)<(r2 & 0xFFFFFFFF):
            pc+=offset
        else:
            pc+=4
    elif func3=="111":
        if (r1 & 0xFFFFFFFF)>=(r2 & 0xFFFFFFFF):
            pc+=offset
        else:
            pc+=4
    return pc

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
        fin_mem_addr = int((fin_mem_addr-int(0x00010000))/4)

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

def jbin_op(asm_ins,registers,pc,mem):
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
    return pc+4    
def sbin_op(binary_instruction,registers,memory,pc):
    
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
    address=int((address-int(0x00010000))/4)
    memory[address]=registers[rs2]
    
    return pc + 4
    
def ubin_op(binary_instruction,registers,pc):
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

def main():
    data_file = sys.argv[1]
    out_file = sys.argv[2]
    with open(data_file,"r") as f:
        data = [i.strip() for i in f.readlines()]

    

    pc=0
    wdata = []
    while (pc<=(len(data)-1)*4):
        
        i=data[int(pc/4)] 
        if i=="00000000000000000000000001100011":
            with open(out_file,"w") as f:
                wdata.append("0b"+pc_str+" ")
                for i in registers:
                    temp="0b"+format(registers[i],"032b")+" "
                    wdata.append(temp)
                wdata.append("\n")  
                for i in wdata:
                    f.write(i)
               
                temp=0x00010000
                for i in memory:
                    f.write("0x000"+format(temp,'X')+":"+"0b"+format(i,"032b")+'\n')
                    temp+=4
                return 
        opcode = i[25:]
        if opcode=="0110011":#R
            pc= rbin_op(i,registers,pc)
        elif opcode=="0010011" or opcode=="0000011" or opcode=="1100111":#I
            pc=ibin_op(i,registers,pc,memory)
        elif opcode=="0100011":#s
            pc=sbin_op(i,registers,memory,pc)
        elif opcode=="1100011":#b
            pc=bbin_op(i,pc,registers)
        elif opcode=="1101111":#j
            pc=jbin_op(i,registers,pc,memory)
        elif opcode=="0110111" or opcode=="0010111":#u
            pc=ubin_op(i,registers,pc)
        pc_str = format(pc,"032b")
        wdata.append("0b"+pc_str+" ")
        for i in registers:
            temp="0b"+format(registers[i],"032b")+" "
            wdata.append(temp)
        
        wdata.append("\n")
        

        
if __name__ == "__main__":
    main()