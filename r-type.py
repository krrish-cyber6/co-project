import pickle 
with open("data.txt","r") as d:
    data = d.readlines()

rData = {"add":["0000000", "000", "0110011"],"sub":["0100000","000","0110011"],"sll":["0000000","001","0110011"],
"slt":["0000000","010","0110011"],"sltu":["0000000","011","0110011"],"xor":["0000000","100","0110011"],
"srl":["0000000","101","0110011"],"sra":["0100000","101","0110011"],"or":["0000000","110","0110011"],
"and":["0000000","111","0110011"]}

for i in data:
    r = i
    l = r.split(" ")
    command = l[0]
    if command not in rData:
        print("Wrong command")
        continue
    l1 = l[1].split(",")
    rs2 = format(int(l1[2][1:]),"05b")
    rs1 = format(int(l1[1][1:]),"05b")
    rd = format(int(l1[0][1:]),"05b")
    funct7 = rData[l[0]][0]
    funct3 = rData[l[0]][1]
    opcode = rData[l[0]][2]
    print(funct7,rs2,rs1,funct3,rd,opcode)
