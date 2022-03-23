a , i = input().split()
for _ in range(int(a)):
    i = int(i)
    op = input()
    if op == "++X" or op == "X++":
        i += 1
    elif op == "--X" or op == "X--":
        i -= 1
print(i)