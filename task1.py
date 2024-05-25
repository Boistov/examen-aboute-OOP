num  = [10, 15, 20, 2, 10, 6]
a = b = num[0]


for i in num:
    if i > a:
        a = i
    elif i < b:
        b = i
print(a - b)

