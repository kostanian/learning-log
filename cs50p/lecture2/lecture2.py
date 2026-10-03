# for i in range(3):
#     print("meow")

# i=0
# while i<3:
#     print("woof")
#     i+=1

# for _ in range (3):
#     print("cool")

# print("meow\n"*3, end="")

# while True:
#     n=int(input("What is the N? "))
#     if n<=0:
#         continue
#     else:
#         break

# for _ in range(n):
#     print(f"{_+1}. auf")

# def main():
#     number=get_number()
#     meow(number)

# def get_number():
#     while True:
#         n=int(input("what the number? "))
#         if n >=1:
#             return n


# def meow(n):
#     for _ in range (n):
#         print(f"{_+1}. meow")

# main()

# students=["Hermione","Harry", "Ron"]
# for student in students:
#     print(student)


# students=["Hermione","Harry", "Ron"]
# for i in range(len(students)):
#     print(i, students[i])

# students=["Hermione","Harry", "Ron", "Draco"]
# houses=["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# students={
#     "Hermione":"Gryffindor",
#     "Harry":"Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco": "Slytherin"
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# students={
#     "Hermione":"Gryffindor",
#     "Harry":"Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco": "Slytherin"
# }

# for student in students:
#     print(student, students[student], sep=", ")

# students=[
#     {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
#     {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
#     {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russel terier"},
#     {"name":"Draco", "house":"Slytherin", "patronus":None},
# ]

# for student in students:
#     print(student["name"], student["house"], sep=", ")


# for _ in range(3):
#     print("#")


# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()


# def main():
#     print_row(4)

# def print_row(width):
#     print ("?" * width)

# main()

def main():
    print_square(3)

def print_square(size):
    for i in range (size):
        for j in range (size):
            print('#', end="")
        print()

main()
