def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = 2
end = 1043

for num in range(start, end):
    if is_prime(num):
        print(num)

