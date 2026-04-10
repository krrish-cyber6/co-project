def signed(n,n1):
    temp=format(n,f"0{n1}b")
    if temp[0]=="1":
        return n-2**n1
    else:
        return n

def rbin_op(bin_instruction, registers):
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
            registers[rd]=(int(signed(registers[rs1])<signed(registers[rs2])))&0xFFFFFFFF
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
            raise KeyError