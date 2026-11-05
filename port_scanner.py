import socket

print("--- Мини сканер портов ---")
target = input("Введите IP адресс (например, 127.0.0.1 ")



print(f"Сканирую {target}...")

for port in range(1, 101):

    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.settimeout(0.5)



    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Порт {port} ОТКРЫТ")


    s.close()


print ("Сканирование завершено.")
