varlist = ['1', '2', '3', '4']

newlist = map(int, varlist)

print(newlist, list(newlist))

numlist = [1, 2, 3, 4]
print(numlist)


def func(num):
    return pow(num, 2)


powlist = map(func, numlist)
print(powlist, list(powlist))
