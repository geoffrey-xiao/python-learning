var1 = 'abcd'
var2 = ['a1', 'b1', 'c1']
var3 = ('A', 'B', 'C', 'D')

res = zip(var1, var2, var3)
print(list(res))

var4 = ['e', 'f', 'g']
var5 = ['E', 'F', 'G']

res1 = zip(var4, var5)

x1, y1 = zip(*zip(var4, var5))
print(list(res1))
print(x1, y1)
