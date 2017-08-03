N = int(input())
if N % 2 == 0:
    STR = '1' * int(N/2)
elif N <= 3:
    STR = '7'
else:
    STR = '7' + '1' * int((N/2) - 1)
print(STR)
