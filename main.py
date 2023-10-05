input_numbers = input("Введіть елементи списку цілих чисел, розділені пробілом: ")
numbers = [int(num) for num in input_numbers.split()]
total_sum = (sum(numbers))
average = total_sum / len(numbers)
print(f"Сума всіх елементів у списку: {total_sum}")
print(f"Середнє арифметичне елементів у списку: {average}")