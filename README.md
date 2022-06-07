# Тестовое задание

Сайт запускается файлом <a href="https://github.com/Grigoriy457/test-projct/blob/main/website.py" target="_blank">`website.py`</a>


Я создал ещё один файл [`start.bat`](https://github.com/Grigoriy457/test-projct/blob/main/start.bat):
1. `taskkill /IM python.exe /f` - закрытие всех запущенных ботов
2. `python website.py` - запуск flask сайт ([`website.py`](https://github.com/Grigoriy457/test-projct/blob/main/website.py))


> Запуск сервиса:
> - Запустите [`start.bat`](https://github.com/Grigoriy457/test-projct/blob/main/start.bat) файла в той же папке где и [`website.py`](https://github.com/Grigoriy457/test-projct/blob/main/website.py)


Необходимые модули (`requirements.txt`):
```
Flask==2.0.2
aiogram==2.16
discord.py==1.7.3
requests==2.27.1
```
