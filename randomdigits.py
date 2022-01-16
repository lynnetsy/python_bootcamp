number_digits = 128
password = {}

for number in range(0, number_digits):
    random_digit = random.randint(0, 9)
    password.append(str(random_digit))