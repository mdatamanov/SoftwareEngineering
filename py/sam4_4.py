import math

def main():
    print("Введите любое количество чисел (разделяйте пробелом):")
    numbers = [float(x) for x in input().split()]
    result = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое: {result:.2f}")

if __name__ == "__main__":
    main()