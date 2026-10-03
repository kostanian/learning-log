# x= int(input("What x?: "))
# y=int(input("What y?: "))

# if x<y:
#     print("X is less then Y")
# elif x>y:
#     print("Y is less then X")
# else:
#     print("X is equal to Y")


# score=int(input("Score: "))
# if score >=90 and score <=100:
#     print("Grade: A")
# elif score>=80 and score<90:
#     print("Grade: B")
# elif score>=70 and score<80:
#     print("Grade: C")
# elif score>=60 and score<70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# x=int(input("x is: "))
# if x%2==0:
#     print("x is even")
# else:
#     print("x is odd")

# def main():
#     x=int(input("What's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False

# main()

# name=input("whats your name? ")

# if name == "Harry":
#     print("Potter")

# elif name=="Hermione":
#     print("Potter")

# elif name=="Ron":
#     print("Potter")

# elif name=="Artur":
#     print("kos")
# else:
#     print("Who?")

name=input("whats your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case ("Hermione"):
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
