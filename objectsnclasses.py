

def dig_pow(n, p):
    num = str(n)
    total = sum([int(num[i]) ** (p + i) for i in range(len(num))])
    return total / n if (total % n) == 0 else -1

def createPhoneNumber(numbers)
numbers = []
a = input(int("enter the numbers")
end