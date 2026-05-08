a = [1, 2, 3, 4, 5]

k = int(input("Enter index for M04: "))

a = a[:k] + [99] + a[k:]

print("M04:", a)