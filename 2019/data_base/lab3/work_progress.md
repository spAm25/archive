#### Таблицы БД до нормализации

Таблица сущностей "**Магазин**"

|  ID  |       Адрес       |
| :--: | :---------------: |
|  1   | ул. Номер 1 д. 10 |
|  2   | ул. Номер 2 д. 13 |

Таблица сущностей "**Покупка - Товар**"

| ID покупки | ID товара |
| :--------: | :-------: |
|     1      |     1     |
|     2      |     2     |

Таблица сущностей "**Магазин - Товар**"

| ID магазина | ID товара |
| :---------: | :-------: |
|      1      |     1     |
|      1      |     2     |

Таблица сущностей "**Товар**"

|  ID  | ID поставщика |    Название    | Кол-во | Дата поставки | Стоимость |
| :--: | :-----------: | :------------: | :----: | :-----------: | :-------: |
|  1   |       2       | Яблоки красные |   2    |   25.10.19    |   1000    |
|  2   |       2       | Яблоки зеленые |   1    |   10.10.19    |   1500    |

Таблица сущностей "**Поставщик**"

|  ID  |       Адрес       |
| :--: | :---------------: |
|  1   | ул. Номер 1 д. 11 |
|  2   | ул. Номер 1 д. 16 |

Таблица сущностей "**Покупка**"

|  ID  | ID работника | ID покупателя | Дата покупки |
| :--: | :----------: | :-----------: | :----------: |
|  1   |      2       |       2       |   31.10.19   |
|  2   |      2       |       2       |   31.10.19   |

Таблица сущностей "**Покупатель**"

|  ID  | Контактные данные | Категория привелегий |
| :--: | :---------------: | :------------------: |
|  1   | +7(999)-333-22-11 |         -10%         |
|  2   | +7(999)-321-22-11 |         -50%         |

Таблица сущностей "**Работник**"

|  ID  | Контактные данные | Должность  |
| :--: | :---------------: | :--------: |
|  1   | +7(999)-123-22-33 |  cashier   |
|  2   | +7(999)-654-22-11 | supervisor |

Таблица сущностей "**Контактные данные**"

|  Номер телефона   |         ФИО          | Адрес |
| :---------------: | :------------------: | :---: |
| +7(999)-333-22-11 | Фамилия Имя Отчество | Адрес |
| +7(999)-321-22-11 | Фамилия Имя Отчество | Адрес |
| +7(999)-123-22-33 | Фамилия Имя Отчество | Адрес |
| +7(999)-654-22-11 | Фамилия Имя Отчество | Адрес |

#### Первая нормальная форма.



Представленные таблицы находятся в первой нормальной форме т.к.

* Порядок строк и столбцов в таблицах не имеет значения.
* Каждое пересечение столбца и строки содержит только 1 значение.
* Каждая строка уникальная  (*неповторяющаяся*).

#### Вторая нормальная форма.



Представленные таблицы находятся в второй нормальной форме т.к. во всех таблицах, неключевые атрибуты зависят только от ключевых атрибутов, а не от других неключевых атрибутов.

#### Третья нормальная форма.



Представленные таблицы находятся в третей нормальной форме т.к. во всех таблицах, все неключевые атрибуты таблиц не находятся в транзитивной связи “один ко многим” с потенциальными ключами таблиц .