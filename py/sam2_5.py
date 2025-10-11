results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1,
           30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
sorted_results = sorted(results)
print("1) Три лучших результата:")
for i, time in enumerate(sorted_results[:3], 1):
    print(f"   {i}. {time} сек")
print("\n2) Три худших результата:")
for i, time in enumerate(sorted_results[-3:][::-1], 1):
    print(f"   {i}. {time} сек")
print("\n3) Все результаты начиная с 10:")
results_from_10 = [time for time in sorted_results if time >= 10]
for i, time in enumerate(results_from_10, 1):
    print(f"   {i}. {time} сек")