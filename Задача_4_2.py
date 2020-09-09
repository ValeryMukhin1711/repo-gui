а = [1, 2, 8, 1, 3, 4, 2, 78, 4, 5]
b = [a[i] for i in range(1, len(a)) if a[i]>a[i-1]]
print (b)
