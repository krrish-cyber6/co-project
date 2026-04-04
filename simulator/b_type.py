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