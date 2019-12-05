opcodes = []
incodes = []
def multiply(a,b,c):
    global opcodes
    #print(a,b,c)
    ans = a * b
    #print("answer",ans)
    opcodes[c] = ans
    
def add(a,b,c):
    global opcodes
    print(a,b,c)
    ans = a + b
    #print("answer",ans)
    opcodes[c] = ans
    
def save_input(a,c):
    global opcodes
    opcodes[c] = a



with open("input.txt") as file:
#with open("test1.txt") as file:
    for line in file:
        incodes= line.rstrip().split(",")
        for c in incodes:
            opcodes.append(int(c))

#print(opcodes)
#opcodes = [3,0,4,0,99]
#opcodes = [1002,4,3,4,33]
#opcodes = [1101,100,-1,4,0]
#opcodes = [1,0,0,0,99]
#opcodes = [2,3,0,3,99]
#opcodes = [1,1,1,4,99,5,6,0,99]

index = 0
while index < len(opcodes):
    #print(opcodes)
    #print(index)
    i = opcodes[index]
    #print("opcode is: " + str(i) + ", index : " + str(index))
    if len(str(i)) > 1 and i != 99:
        i_pad = str(i).zfill(5)
        i = int(i_pad[-2:])
        par1_mode = int(i_pad[2])
        par2_mode = int(i_pad[1])
        par3_mode = int(i_pad[0])
        if par1_mode == 0:
            par1 = opcodes[opcodes[index+1]]
        elif par1_mode == 1:
            par1 = opcodes[index+1]
        if i != 4 and i != 3:
            if par2_mode == 0:
                par2 = opcodes[opcodes[index+2]]
            elif par2_mode == 1:
                par2 = opcodes[index+2]
            if par3_mode == 0:
                par3 = opcodes[index+3]
            elif par3_mode == 1:
                par3 = opcodes[index+3]

    #print(index, opcodes)
        if i == 2:
            print('miltiplying -')
            #print(par1_mode,par2_mode,par3_mode)
            #print(par1,par2,par3)
            multiply(par1,par2,par3)
            index+=4
        elif i == 1:
            print('adding -')
            #print(par1_mode,par2_mode,par3_mode)
            #print(par1,par2,par3)
            add(par1,par2,par3)
            index+=4
        elif i == 99:
            print('halt -')
            break
        elif i == 3:
            print("input -")
            in_value = input("enter a single integer: ")
            save_input(in_value,par1)
            index+=2
        elif i == 4:
            print("output -")
            out_value = par1
            print(out_value)
            if out_value != 0:
                print("************************")
            index+=2
        else:
            print('meh')
            index+=1
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
            if out_value != 0:
                print("************************")

            index+=2
        else:
            print('meh')
            index+=1

print(opcodes)
#print(opcodes[0])
output =  opcodes[0]

print('done')

