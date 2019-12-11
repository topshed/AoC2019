incodes = []
opcodes = [0] *10000
def multiply(a,b,c):
    global opcodes
    #print(a,b,c)
    ans = a * b
    #print("answer",ans)
    opcodes[c] = ans
    
def add(a,b,c):
    global opcodes
    #print(a,b,c)
    ans = a + b
    #print("answer",ans)
    opcodes[c] = ans
    
def save_input(a,c):
    global opcodes
    print("saving ", a , " to position ", c)
    opcodes[c] = a


#with open("input.txt") as file:
with open("input.txt") as file:
    for line in file:
        incodes= line.rstrip().split(",")
        index = 0
        for c in incodes:
            opcodes[index] = int(c)
            index+=1


relative_base = 0
index = 0
while index < len(opcodes):
    #print(opcodes)
    #print(index)
    i = opcodes[index]
    print("opcode is: " + str(i) + ", index : " + str(index) + ", rel base: " + str(relative_base))
    if len(str(i)) > 1 and i != 99:
        i_pad = str(i).zfill(5)
        i = int(i_pad[-2:])
        par1_mode = int(i_pad[2])
        par2_mode = int(i_pad[1])
        par3_mode = int(i_pad[0])
        
        if par1_mode == 0: # position mode
            par1 = opcodes[opcodes[index+1]]
        elif par1_mode == 1: # imediate mode
            par1 = opcodes[index+1]
        elif par1_mode == 2: # relative mode
            if i != 3:
                par1 = opcodes[opcodes[index+1] + relative_base]
        
            else:
                par1 = opcodes[index+1] + relative_base
                #par1 = opcodes[index+1] + relative_base
            
        if i != 4 and i != 3 and i != 9:
            if par2_mode == 0: #position mode
                par2 = opcodes[opcodes[index+2]]
            elif par2_mode == 1: # imediate mode
                par2 = opcodes[index+2]
            elif par2_mode == 2: # relative mode
                par2 = opcodes[opcodes[index+2] + relative_base]
                #par2 = opcodes[index+2] + relative_base
            if i != 5 and i != 6 and i != 9:
                if par3_mode == 0:
                    par3 = opcodes[index+3]
                elif par3_mode == 1:
                    par3 = opcodes[index+3]
                elif par3_mode == 2: # relative mode
                    par3 = opcodes[opcodes[index+3] + relative_base]


        print("par1 ", par1, " index+1 ", index+1, " next: ", opcodes[index+1]+relative_base, " opcode[0]: ",opcodes[0])

    #print(index, opcodes)
        if i == 2:
            #print('miltiplying -')
            #print(par1_mode,par2_mode,par3_mode)
            #print(par1,par2,par3)
            multiply(par1,par2,par3)
            index+=4
        elif i == 1:
            #print('adding -')
            #print(par1_mode,par2_mode,par3_mode)
            #print(par1,par2,par3)
            add(par1,par2,par3)
            index+=4
        elif i == 99:
            print('halt -')
            break
        elif i == 3:
            print("input -")
            in_value = int(input("enter a single integer: "))
            save_input(in_value,par1)
            
            index+=2
        elif i == 4:
            print("output -")
            out_value = par1
            print(out_value)
            index+=2
        elif i == 5:
            if par1 != 0:
                index = par2
            else:
                index+=3
        elif i == 6:
            if par1 == 0:
                index = par2
            else:
                index+=3
        elif i == 7:
            if par1 <  par2:
                save_input(1,par3)
            else:
                save_input(0,par3)
            index+=4
        elif i == 8:
            print(par1, par2,par3)
            if par1 == par2:
                save_input(1,par3)
            else:
                save_input(0,par3)
            index+=4
        elif i == 9:
            relative_base = relative_base + par1
            #relative_base = relative_base + opcodes[index+1]
            index+=2
        else:
            print('meh')
            index+=1
    elif i == 99:
        print("halt")
        break
    else:

        if i == 2:
            print('miltiplying')

            par1 = opcodes[opcodes[index+1]]
            par2 = opcodes[opcodes[index+2]]
            par3 = opcodes[index+3]
            multiply(par1,par2,par3)
            index+=4
        elif i == 1:
            print('adding')
 
            par1 = opcodes[opcodes[index+1]]
            par2 = opcodes[opcodes[index+2]]
            par3 = opcodes[index+3]
            print('adding', par1, par2,par3)
            add(par1,par2,par3)
            index+=4
        elif i == 99:
            print('halt')
            break
        elif i == 3:
            print("input")
            par1 = opcodes[index+1]
            #print(par1)
            in_value = int(input("enter a single integer: "))
            save_input(in_value,par1)
            index+=2
        elif i == 4:
            print("output")
            par1 = opcodes[index+1]
            out_value = opcodes[par1]
            print(out_value)
            #if out_value != 0:
             #   print("************************")

            index+=2
        elif i == 5:
            par1 = opcodes[opcodes[index+1]]
            par2 = opcodes[opcodes[index+2]]
            if par1 != 0:
                index = par2
            else:
                index+=3
        elif i == 6:
            par1 = opcodes[opcodes[index+1]]
            par2 = opcodes[opcodes[index+2]]
            if par1 == 0:
                index = par2
            else:
                index+=3
        elif i == 7:
            par1 = opcodes[opcodes[index+1]]
            par2 = opcodes[opcodes[index+2]]
            par3 = opcodes[index+3]
            if par1 <  par2:
                save_input(1,par3)
            else:
                save_input(0,par3)
            index+=4
        elif i == 8:
            par1 = opcodes[opcodes[index+1]]
            par2 = opcodes[opcodes[index+2]]
            par3 = opcodes[index+3]
            if par1 == par2:
                save_input(1,par3)
            else:
                save_input(0,par3)
            index+=4
        elif i == 9:
            par1 = opcodes[index+1]
            relative_base = relative_base + par1
            index+=2
        else:
            print('meh!')
            index+=1

#print(opcodes)
#print(opcodes[0])
output =  opcodes[0]

print('done')

