
def plus(a,b):
    result=a+b
    return result


def minus(a,b):
    result=a-b
    return result

def multi(a,b):
    result=a*b
    return result

def devide(a,b):
    result=a/b
    return result

inp=input("Expression: ").strip()
first_num=float(inp.split()[0])
last_num=float(inp.split()[-1])
if inp.split()[1]=="+":
    result_plus=plus(first_num,last_num)
    print(round(result_plus,1))

elif inp.split()[1]=="-":
    result_minus=minus(first_num,last_num)
    print(round(result_minus,1))

elif inp.split()[1]=="*":
    result_mult=multi(first_num,last_num)
    print(round(result_mult,1))

elif inp.split()[1]=="/":
    result_division=devide(first_num,last_num)
    print(round(result_division,1))
else:
    print('wrong input')