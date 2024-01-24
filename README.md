# Cat Charity Fund
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=bc8429)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-green)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=REST&logoColor=ffffff&color=bc2929)](https://docs.pydantic.dev/latest/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GoogleAPI](https://img.shields.io/badge/-GoogleAPI-464646?style=flat&logo=Google&logoColor=4285F4&color=800000)](https://support.google.com/googleapi/?hl=en#topic=7014522)

Проект Cat Charity Fund - это веб-приложение, которое представляет собой фонд, собирающий пожертвования на различные целевые проекты, связанные с поддержкой кошачьей популяции. Фонд может иметь несколько проектов, каждый из которых имеет своё название, описание и сумму, которую необходимо собрать. Пожертвования в проекты поступают по принципу First In, First Out, то есть все пожертвования идут в проект, открытый раньше других. Когда этот проект набирает необходимую сумму и закрывается, пожертвования начинают поступать в следующий проект.

Основной целью проекта является помощь кошачьей популяции и привлечение внимания к проблеме бездомных животных. Проект Cat Charity Fund предоставляет удобный и прозрачный механизм для сбора пожертвований и распределения их между различными проектами.

Upd:
- Добавлена возможность формирования отчёта в гугл-таблице. В таблице выводятся закрытые проекты, отсортированные по скорости сбора средств — от тех, что закрылись быстрее всего, до тех, что долго собирали нужную сумму.


## Основные функции платформы
- Просмотр существующих проектов (_доступно всем_).
-  Создавать, удалять и обновлять проекты могут только _администраторы (суперпользователи)_.
-  Жертвование средств на текущий проект.
- Работа с GoogleAPI.

## Технологии
- Python 3.10
- FastAPI 0.78.0
- Pydantic 1.9.1
- SQLAlchemy 1.4
- google-api-core==2.15.0

## Использование
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Ozxar69/cat_charity_fund.git
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    . venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Env
На основе файла envexample создайте файл .env и заполните его

## Миграции
Применить миграции:


```commandline
alembic upgrade head
```

Запуск проекта:

```commandline
uvicorn app.main:app --reload
```

Автор: [Ozxar69](https://github.com/Ozxar69)
