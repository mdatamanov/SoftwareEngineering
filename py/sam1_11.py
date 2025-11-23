def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
def main():
    fib_gen = fib(200)
    fib_numbers = list(fib_gen)
    print(f"200-е число Фибоначчи: {fib_numbers[-1]}")
    print(f"Первые 10 чисел: {fib_numbers[:10]}")
    print(f"Последние 5 чисел: {fib_numbers[-5:]}")
if __name__ == "__main__":
    main()