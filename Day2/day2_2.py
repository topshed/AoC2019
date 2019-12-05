opcodes = []
def multiply(a,b,c):
    global opcodes
    #print(a,b,c)
    ans = int(opcodes[int(a)]) * int(opcodes[int(b)])
    #print("answer",ans)
    opcodes[int(c)] = str(ans)
def add(a,b,c):
    global opcodes
    #print(a,b,c)
    ans = int(opcodes[int(a)]) + int(opcodes[int(b)])
    #print("answer",ans)
    opcodes[int(c)] = str(ans)

output = 0

for noun in range(100):
    for verb in range(100):
        #print(noun,verb)
        with open("input_orig.txt") as file:
        #with open("test1.txt") as file:
            for line in file:
                opcodes= line.rstrip().split(",")
        opcodes[1] = str(noun)
        opcodes[2] = str(verb)
        #print(opcodes)
        index = 0
        while index < len(opcodes):
            i = opcodes[index]
            #print(index, opcodes)
            
            if i == '2':
                #print('miltiplying')
                multiply(opcodes[index+1],opcodes[index+2],opcodes[index+3])
                index+=4
            elif i == '1':
                #print('adding')
                add(opcodes[index+1],opcodes[index+2],opcodes[index+3])
                index+=4
            elif i == '99':
                #print('halt')
                break
            else:
                #print('meh')
                index+=1

        #print(opcodes)
        #print(opcodes[0])
        output =  opcodes[0]
        #print(noun, verb, output)
        if  output == '19690720':

            print(noun,verb)
print('done')

