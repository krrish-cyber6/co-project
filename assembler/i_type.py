from store import Register_Mapping

instr = { "lw" :["010","0000011"], #0-index: funct3,  1-index: opcode
         "addi" :["000","0010011"],
         "sltiu":["011","0010011"],
         "jalr" :["000","1100111"]  }


inp = "addi x5, x3, -1"

#Function to convert immediate value to binary
'''def imm_to_bin(imm):
    imm = int(imm)
    if imm >= 0:
        return format(imm, "012b")
    else:
        return format( ~imm + 1, "012b")''''

#Function to convert register value to binary            
def reg_to_bin(reg):
    return format(int(reg), "05b")     
          
#Function to convert instructions to binary     
def itoBinary(inp):
    cmd = []
    cmd.append(inp.replace(",","").split())
    try:
        for x in cmd:
            b = instr.get(x[0])
            funct3, opcode = b     
            if x[0] == "lw":

                rd = reg_to_bin(x[1][1:])   
                imm, rs1 = x[2].replace(")", "").split("(") #Removing brackets 
                rs = reg_to_bin(rs1[1:])    
                imm = imm_to_bin(imm)
        
            else:
                rd = reg_to_bin(x[1][1:])
                rs = reg_to_bin(x[2][1:])
                imm = imm_to_bin(x[3])
                
        print(imm + rs + funct3 + rd + opcode)
    except:
        raise Exception("Invalid assembly command")
itoBinary("addi x3, x2, -3")          

                      
                        

              



