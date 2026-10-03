inp=input().split()
new_inp=[]

count = 0
while count<len(inp):
    if count<len(inp)-1:
        new_inp.append(inp[count]+"...")
    else:
        new_inp.append(inp[count])
    count=count+1
    
print(''.join(new_inp))


#Решение2
# inp=input().replace(" ", "...")
# print(inp)
    
    
