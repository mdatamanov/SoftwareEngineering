def create_special_set(numbers):
    result_set = set()
    from collections import Counter
    count_dict = Counter(numbers)
    for num, count in count_dict.items():
        result_set.add(num)
        if count > 1:
            for repeat_count in range(2, count + 1):
                str_representation = str(num) * repeat_count
                result_set.add(str_representation)

    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print("list_1 =", list_1)
set_1 = create_special_set(list_1)
print("Результат:", set_1)
print("\nlist_2 =", list_2)
set_2 = create_special_set(list_2)
print("Результат:", set_2)
print("\nlist_3 =", list_3)
set_3 = create_special_set(list_3)
print("Результат:", set_3)
