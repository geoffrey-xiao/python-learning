varset = {1, 2, 3, 4}
newset = {i << 1 for i in varset}

var1 = {1, 2, 3}
var2 = {4, 5, 6}

# news = set()
# for i in var1:
#     for j in var2:
#         news.add(i+j)
news = {i + j for i in var1 for j in var2 if i % 2 == 0}
# print(newset)
print(news)
