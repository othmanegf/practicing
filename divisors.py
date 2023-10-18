n = int(input("Enter an integer: "))
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

if len(divisors) > 0:
    print("The divisors of", n, "are:", divisors)
    print("Number of divisors found:", len(divisors))
else:
    print(n, "is a prime number, it has only two divisors: 1 and itself.")