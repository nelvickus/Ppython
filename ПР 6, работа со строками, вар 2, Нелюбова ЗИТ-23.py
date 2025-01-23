
input_string = input("Введите строку: ")
count_colons = input_string.count(':')
output_string = input_string.replace(':', '%')

print("Измененная строка:", output_string)
print("Количество замен:", count_colons)
