n = int(input("Enter->"))

for i in range(1, n + 1):
    if i <= n // 2:
        for j in range(i):
            print(i, end=' ')
        print()
    else:
        for j in range(n - i + 1):
            print(i, end=' ')
        print()






