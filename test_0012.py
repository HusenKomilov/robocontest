n = int(input())

not_prime = [i for i in range(n + 1)]

not_prime[1] = 0

i = 2
while i <= n:
    if not_prime[i] != 0:
        j = i + i

        while j <= n:
            not_prime[j] = 0
            j = j + i
    i += 1

not_prime = [i for i in not_prime if i != 0]
h = "Ali" if len(not_prime) % 2 else "Bobur"
print(h)
