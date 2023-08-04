## Пульт охраны банка

Пульт охраны - это сайт, который можно подключить к своей базе данных, с визитами и пропусками сотрудников.  

На сайте 2 раздела:

#### Активные карты доступа - выводит сотрудников, у которых есть активный пропуск.  

В этом разделе можно выбрать любого сотрудника и увидеть его историю посещений в хранилище.  

#### Список пользователей в хранилище - выводит сотрудников которые находятся в хранилище.  

В разделе выводится дата и длительность посещения.  

## Установка

Скачайте архив, или сделайте клон репозитория на ваш компьютер.  

В консоли введите команду по установке библиотек:  

```
pip install -r requirements.txt
```

В корневой папке создайте файл sensitive_information.env и присвойте переменным значения для доступа к базе данных.  

Ниже перечислены переменные для подключения базы данных.  

```
ENGINE
HOST
PORT
NAME
USER
PASSWORD
SECRET_KEY
DEBUG
DEFAULT_AUTO_FIELD
TIME_ZONE
LANGUAGE_CODE
```

Если переменной DEBUG присвоить значение True, то при появлении ошибки запроса пользователь увидит отладочную информацию.  

## Запуск

Для запуска проекта введите в консоль команду старта:  

```
python manage.py runserver
```

И переходите по выведенному ip.
