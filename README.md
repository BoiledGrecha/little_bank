# little_bank

Сначала запускаем generate.py, создаётся тестовая база.

После, можем запустить файл admin.py в котором будет отражено текущее состояние базы и дальнейшие возможные инструкции.

Так же можем запустить файл user.py, где нам будет предложено следовать инструкциям.
При каждом переводе денег на другой счёт создаётся соответствующая запись с временнОй пометкой в файле log.txt.
Чтоб оградить систему от перегрузки после некоторых операций введены временные задержки.
