# This short program was extracted from the book Automate the boring stuff with Python.
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number //2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1


n= input("INTRODUCE TU NÚMERO: ")
while n != 1:
    n = collatz (int(n))






