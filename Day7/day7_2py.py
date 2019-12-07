import itertools
from queue import Queue
from threading import Thread
from time import sleep

result = [1]
finished = False

def software(in_arg,in_q_id, out_q_id,amp):
    #print("starting ", amp)
    global result
    global finished
    opcodes = []
    input_counter =0
    incodes = []
    #with open("input.txt") as file:
    with open("input.txt") as file:
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
    #opcodes = [3,9,8,9,10,9,4,9,99,-1,8] # 1 if =8
    #opcodes = [3,3,1108,-1,8,3,4,3,99] # 1 if =8
    #opcodes = [3,3,1107,-1,8,3,4,3,99] # 1 if < 8
    #opcodes = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9] #1 if > 0
    #opcodes = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1] # 1 if > 0
    #opcodes = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    index = 0
    while index < len(opcodes):
        #print(amp, opcodes)
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
                if i != 5 and i != 6:
                    if par3_mode == 0:
                        par3 = opcodes[index+3]
                    elif par3_mode == 1:
                        par3 = opcodes[index+3]

        #print(index, opcodes)
            if i == 2:
                #print('miltiplying -')
                #print(par1_mode,par2_mode,par3_mode)
                #print(par1,par2,par3)
                #opcodes = multiply(par1,par2,par3,opcodes)
                opcodes[par3] = par1 * par2
                index+=4
            elif i == 1:
                #print('adding -')
                #print(par1_mode,par2_mode,par3_mode)
                #print(par1,par2,par3)
                #opcodes =add(par1,par2,par3,opcodes)
                opcodes[par3] = par1 + par2
                index+=4
            elif i == 99:
                #print('halt -')
                break
            elif i == 3:
                #print(amp , " waiting for input -")
                #in_value = input("enter a single integer: ")
                if input_counter == 0 and amp == "A":
                    in_value = in_arg
                    #in_value = input("enter a single integer: ")
                elif input_counter == 0 and amp != "A":
                    in_value = in_arg
            
                if input_counter == 1 and amp == "A":
                    in_value = 0
                elif input_counter == 1 and amp != "A":
                    in_value = in_q_id.get()
                    
                if input_counter > 1:
                    in_value = in_q_id.get()

                #print( amp, " got input ", str(in_value))
                #opcodes = save_input(in_value,par1,opcodes)
                opcodes[par1] = in_value
                index+=2
                input_counter+=1
            elif i == 4:
                #print(amp, "output -")
                out_value = par1
                out_q_id.put(out_value)
                #print(amp, " output ", out_value)
               # if amp == "E":
                #    print(amp, " output: ",out_value)
                #if out_value != 0:
                   # print("************************")
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
                    #opcodes = save_input(1,par3,opcodes)
                    opcodes[par3] = 1
                else:
                    #opcodes = save_input(0,par3,opcodes)
                    opcodes[par3] = 0
                index+=4
            elif i == 8:
                if par1 == par2:
                    #opcodes = save_input(1,par3,opcodes)
                    opcodes[par3] = 1
                else:
                    #opcodes = save_input(0,par3,opcodes)
                    opcodes[par3] = 0
                index+=4   
            else:
                print('meh')
                index+=1
        elif i == 99:
            #print("halt")
            break
        else:

            if i == 2:
                #print('miltiplying')

                par1 = opcodes[opcodes[index+1]]
                par2 = opcodes[opcodes[index+2]]
                par3 = opcodes[index+3]
                #opcodes = multiply(par1,par2,par3,opcodes)
                opcodes[par3] = par1 * par2
                index+=4
            elif i == 1:
                #print('adding')
     
                par1 = opcodes[opcodes[index+1]]
                par2 = opcodes[opcodes[index+2]]
                par3 = opcodes[index+3]
                #opcodes = add(par1,par2,par3,opcodes)
                opcodes[par3] = par1 + par2
                index+=4
            elif i == 99:
                #print('halt')
                break
            elif i == 3:
                #print(amp ," waiting for input")
                par1 = opcodes[index+1]
                if input_counter == 0 and amp == "A":
                    in_value = in_arg
                    #in_value = int(input("enter a single integer: "))
                elif input_counter == 0 and amp != "A":
                    in_value = in_arg
            
                if input_counter == 1 and amp == "A":
                    in_value = 0
                elif input_counter == 1 and amp != "A":
                    in_value = in_q_id.get()
                    
                if input_counter > 1:
                    in_value = in_q_id.get()
                #print(amp, " got input ", in_value)
                #opcodes = save_input(in_value,par1,opcodes)
                opcodes[par1] = in_value

                index+=2
                input_counter+=1
            elif i == 4:
                
                par1 = opcodes[index+1]
                out_value = opcodes[par1]
                out_q_id.put(out_value)
                #print(amp, " output ", out_value)
                #if amp == "E":
                 #   print(amp, " output: ",out_value)
                #if out_value != 0:
                    #print("************************")

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
                    #opcodes = save_input(1,par3,opcodes)
                    opcodes[par3] = 1
                else:
                    #opcodes = save_input(0,par3,opcodes)
                    opcodes[par3] = 0
                index+=4
            elif i == 8:
                par1 = opcodes[opcodes[index+1]]
                par2 = opcodes[opcodes[index+2]]
                par3 = opcodes[index+3]
                if par1 == par2:
                    #opcodes = save_input(1,par3,opcodes)
                    opcodes[par3] = 1
                else:
                    #opcodes = save_input(0,par3,opcodes)
                    opcodes[par3] = 0
                index+=4   
            else:
               # print('meh!')
                index+=1

    #print(opcodes)
    #print(opcodes[0])
    #output =  opcodes[0]
    #print("Final >>>>>>>>>",out_value)
    #print(amp, ' Done')
    if amp == "E":
        finished = True
        result.append(out_value)
    #return(out_value)
#phase_setting = [0,1,2,3,4] #part 1
phase_setting = [5,6,7,8,9]

to_test = itertools.permutations(phase_setting,5)

for p in to_test: 
#p = [9,7,8,5,6]
    start_length = 0
    print(p)
    qA = Queue()
    qB = Queue()
    qC = Queue()
    qD = Queue()
    qE = Queue()
    tA = Thread(target = software, args=(p[0],qE,qA,"A",))
    tB = Thread(target = software, args=(p[1],qA,qB,"B",))
    tC = Thread(target = software, args=(p[2],qB,qC,"C",))
    tD = Thread(target = software, args=(p[3],qC,qD,"D",))
    tE = Thread(target = software, args=(p[4],qD,qE,"E",))
    tA.start()
    tB.start()
    tC.start()
    tD.start()
    tE.start()
    #print(max(result))
    #print(result)
    
    while not finished :
        sleep(0.1)
    finished = False
print(max(result))