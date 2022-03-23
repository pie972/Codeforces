A, B, X = map(int, input().split())
 
r = pow(10,9)+1
l = 0
average = (l + r)//2
while r-l > 1:
    average = (r + l)//2
    if A * average+B * len(str(average)) > X:
        r = min(average, r)
    else:
        l = average
print(l)