import random
import string

print("--- Генаратор паролей ---")
length = int(input("Введите длину пароля (например, 12): "))


chars = string.ascii_letters + string.digits + "!@#$%^&*"

password = ""
for i in range(length):
    password += random.choice(chars)

print(f"Ваш пароль: {password}")
