valid = []

def test4(n):
    result = True
    digits=[]
    for x in str(n):
        digits.append(int(x))
    for j in range(1,len(digits)):
        
        if digits[j] >= digits[j-1]:
            pass
            #print(str(digits[j]) + " is >= " + str(digits[j-1]))
        else:
            result = False
            #print(str(digits[j]) + " not >= " + str(digits[j-1]))
    return(result)

def test3(n):
    result = False
    foundtwo = False
    digits=[]
    for x in str(n):
        digits.append(int(x))
    for j in range(0,6):
        #print(j, len(digits))
        if j < 4:
            if digits[j] == digits[j+1]:
                result = True
                
                if digits[j+1] == digits[j+2] or digits[j-1] == digits[j]:
                    if not foundtwo:
                        result = False
                else:
                    foundtwo = True
            
        elif j == 4:
            if digits[j] == digits[j+1] and digits[j] != digits[j-1]:
                result = True

    return(result)

for i in range(273025,767253):
    if test3(i) and test4(i):
        valid.append(i)
print("done")
print(len(valid))
'''
assert test4(223450) == False
assert test4(111111) == True
assert test3(111111) == True
assert test3(223450) == True
assert test3(123450) == False
'''
assert test3(112233) == True
assert test3(123444) == False
assert test3(111122) == True

