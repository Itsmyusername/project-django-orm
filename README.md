## Пульт охраны банка

Это внутренный репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то не сможете его запустить, т.К. у вас нет доступа к БД, но сможете свободно использовать код верстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удаленной БД с визитами, карточками пропуска сотрудников нашего банка.

## Как установить?

Запустите:
```python
pip3 install -r requirements.txt
```

Создайте следующие переменные окружения согласно шаблона:
Пример: ```DATABASE_URL=postgres://DB_USER:DB_PASSWORD@DB_HOST:DB_PORT/DB_NAME```

Затем:
```python
python manage.py runserver youserver:port
```

DEBUG - True для включения режима отладки, False - для отключения
ALLOWED_HOSTS - доступный хост для сайта.
