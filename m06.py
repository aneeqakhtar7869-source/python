line = input("Enter line for M06: ")

words = line.split()

longest = max(words, key=len)

print("M06:", longest, len(longest))