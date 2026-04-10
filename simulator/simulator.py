registers = {
    "00001": 0,
    "00010": 0,
    "00011": 0,
    "00100": 0,
    "00101": 0,
    "00110": 0,
    "00111": 0,
    "01000": 0,
    "01001": 0,
    "01010": 0,
    "01011": 0,
    "01100": 0,
    "01101": 0,
    "01110": 0,
    "01111": 0,
    "10000": 0,
    "10001": 0,
    "10010": 0,
    "10011": 0,
    "10100": 0,
    "10101": 0,
    "10110": 0,
    "10111": 0,
    "11000": 0,
    "11001": 0,
    "11010": 0,
    "11011": 0,
    "11100": 0,
    "11101": 0,
    "11110": 0,
    "11111": 0
}
#r-type part

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
            raise KeyError