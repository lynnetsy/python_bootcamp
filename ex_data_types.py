#Vamos a ver la diferencia con la que se maneja en python los strings y enteros

two_digit_numbers = (input("Introduce 2 numeros\n"))

print(type(two_digit_numbers))

first_digit = two_digit_numbers[0]
second_digit = two_digit_numbers[1]

result = first_digit + second_digit
result_int = int(first_digit) + int(second_digit)

print(result)
print(result_int)