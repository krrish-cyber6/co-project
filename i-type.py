#def itype(command):
instr = { "lw" :["010","0000011"], #0-index: funct3,  1-index: opcode
         "addi" :["000","0010011"],
         "sltiu":["011","0010011"],
         "jalr" :["000","1100111"]  }

# Load instructions to program
S = []
def load(): 
        '''with open("assembly.txt",'r') as fin:
            L = fin.readlines()
            for i in L:
                j = i.replace(",","").split()
                S.append(j)'''
        L = "addi x2, x3, 10"
        j = L.replace(",","").split()
        S.append(j)
        print(S)    
load()

#Function to convert immediate value to binary
def imm_to_bin(imm):
    return format(int(imm),"012b")
            
     

              


