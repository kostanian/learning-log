def ask_number(prompt):
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print("Нужно число. Попробуйте ещё раз.")

def ask_people(prompt):
    while True:
        text = input(prompt)
        try:
            value = int(text)
            if value >= 1:
                return value
            else:
                print("Нужно число не меньше 1. Попробуйте ещё раз.")
        except ValueError:
            print("Нужно число. Попробуйте ещё раз.")
        


bill = ask_number("Сумма счёта: ")
tip_percent = ask_number("Чаевые, %: ")
people = ask_people("Сколько человек: ")

total = bill * (1 + tip_percent / 100)
each = total / people
print(f"Каждый платит: {each:.2f}")
