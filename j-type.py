import pickle
with open("data.txt","r") as d:
    data = d.readlines()


r="jal x4,8"
for i in [0]:
    # r = i
    l = r.split(" ")
    l1 = l[1].split(",")
    command = l[0]
    if command!="jal":
        print("Wrong command")
        continue
    if int(l1[1][:])%2==1:
        print("Odd immediate")
        continue
    
    
    rd = format(int(l1[0][1:]),"05b")
    offset = format(int(l1[1][:])>>1,"021b")
    imm20 = offset[0]
    imm10_1 = offset[10:20]
    imm11 = offset[9]
    imm19_12 = offset[1:9]
    print(imm20,imm10_1,imm11,imm19_12,rd,"1101111")
# 0 0000001000 0 00000000 01011 1101111
# 0 0000010000 0 00000000 01011 1101111