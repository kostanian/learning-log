def main():
    num1=float(input("Write number 1"))
    num2=float(input("Write number 2"))
    sum=total(num1,num2)
    print(sum)


def total (a,b):
    return round(a + b,2)

main()