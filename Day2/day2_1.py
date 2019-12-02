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

with open("input.txt") as file:
#with open("test1.txt") as file:
    for line in file:
        opcodes= line.rstrip().split(",")
print(opcodes)
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

print(opcodes)
print(opcodes[0])
