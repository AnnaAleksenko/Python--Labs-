import requests


response = requests.get('https://api.github.com')
r = requests.post('https://httpbin.org/post', data={'key':'value'})
resp = requests.options('https://pythonexamples.org/')

with open("results.txt", "w", encoding="utf-8") as f:
    f.write("GET" + "\n")
    f.write(f'Ответ сервера:{response.status_code},{response.reason}'+ "\n")
    f.write(f'Заголовки ответа: {response.headers} + "\n"')
    f.write(f'Содержимое ответа:{response.text} + "\n"' + "\n")

    f.write("POST" + "\n")
    f.write(f'Ответ сервера:{r.status_code},{r.reason}' + "\n")
    f.write(f'Заголовки: {r.headers}' + "\n")
    f.write(f'Содержимое ответа: {r.json()}' + "\n")

    f.write("OPTION" + "\n")
    f.write(f'Ответ сервера:{resp.status_code},{resp.reason}' + "\n")
    f.write(f'Заголовки: {resp.headers}' + "\n")
    f.write(f'Содержимое ответа:{resp.text} + "\n"')
