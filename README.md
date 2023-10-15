# Новое русское вино

Скрипт запускает сайт магазина авторского вина "Новое русское вино"  
с возможностью изменять данные сайта путем загрузки .xlsx файла через терминал

## Устновка и активация виртуального окружения(env)

В терминале, в корневой папке проекта создаем вирутальное окружение и устанавливаем зависимости:

```console
$ poetry install
```

Активируем виртуальное окружение:

```console
$ poetry shell
```

Библиотеки официально поддерживают Python 3.5+

## Запуск

Для запуска в скрипта потребуется создать в корневой директории проекта файл .env  
и обозначить в нем переменную виртульного окружения (DRINKS_PATH) содержащую путь основного(конфигурационного) 
файла с данными для сайта:

![Screenshot](https://github.com/valhallajazzy/wine/blob/main/screenshots/env.png width="300" height="300")
![Screenshot](https://github.com/valhallajazzy/wine/blob/main/screenshots/vatiable.png)

- Запустите сайт из корневой директроии командой:

```console
$ python3 main.py
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Изменение файла данных сайта

Если вы хотите запустить сайт используя другой файл данных через терминал  
вам следует указать новый путь к файлу командой:

```console
$ python3 main.py -p 'ваш путь к файлу'
```
или
```console
$ python3 main.py --path 'ваш путь к файлу'
```

Если вы хотите изменить конфигурационный файл запуска, то следует указать новый путь  
в переменной DRINKS_PATH в файле .env

![Screenshot](https://github.com/valhallajazzy/wine/blob/main/screenshots/vatiable.png)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

