def convert(number):
    res = ""
    if number % 3 == 0:
        res += "Pling"
    if number % 5 == 0:
        res += "Plang"
    if number % 7 == 0:
        res += "Plong"
    if (number % 3 != 0) and (number % 5 != 0) and (number % 7 != 0):
        res = str(number)
    return res


print(convert(28))