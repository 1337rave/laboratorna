input_numbers = input("Введіть елементи списку цілих чисел, розділені пробілами: ")
numbers = [int(num) for num in input_numbers.split()]
target_number = int(input("Введіть число для пошуку: "))
count = numbers.count(target_number)
print(f"Число {target_number} зустрічається в списку {count} разів.")
