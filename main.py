n = int(input("Give a n₀: "))

if n <= 0:
    print("n₀ have to be greater than 0")
else:
    steps = 0
    while n != 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    print(1)
    print(f"Steps : {steps}")

    
