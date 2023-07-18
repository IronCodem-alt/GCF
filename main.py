def gcf(a, b):
    if b == 0:
        return a

    else:
        return gcf(b, a % b)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print(gcf(num1, num2))
