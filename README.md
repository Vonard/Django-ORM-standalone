# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД. 

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка. 

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Что бы начать работу, будет необходимо создать в папке проекта файл `.env` и вставить следующее:

```dotenv
DATABASE_HOST=Адрес базы данных
DB_USER_PASSWORD=Пароль пользователя
SITE_SECRET_KEY=Секретный ключ
DATABASE_NAME=Имя базы данных
DATABASE_USER=Имя пользователя
DATABASE_PORT=Порт базы данных
DATABASE_ENGINE=Тип базы данных
```

### Как запустить

Для получения количества всех и активных пропусков нужно запустить `main.py`:
```
python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).