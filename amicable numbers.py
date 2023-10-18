M = int(input("Enter a first integer : "))
N = int(input("Enter a second integer : "))

sum_M = 0
for i in range(2, M // 2 + 1):
    if M % i == 0:
        sum_M += i

sum_N = 0
for i in range(2, N // 2 + 1):
    if N % i == 0:
        sum_N += i

A = sum_M == N and sum_N == M

if A:
    print(M , "and", N ,"are amicable numbers.")
else:
    print(M , "and" , N ,"are not amicable numbers.")
