# filter过滤器

varlist = [1, 4, 6, 9, 8]


def myfunc(num):
    if (num % 2 == 0):
        return True
    else:
        return False


newlist = filter(myfunc, varlist)
print(list(newlist))
