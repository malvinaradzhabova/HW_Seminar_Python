"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet


args = ["ping", "yandex.ru"]
ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
print(ya_ping.stdout)
for line in ya_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result["encoding"]))

args = ["ping", "youtube.com"]
yt_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
print(yt_ping.stdout)
for line in yt_ping.stdout:
    result = chardet.detect(line)
    print(line.decode(result["encoding"]))
