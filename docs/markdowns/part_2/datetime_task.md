# Обработка форматов даты и времени. Модули time, datetime

## Модуль time

!!! tip inline end "Unix-time"

    <a href="https://time.is/ru/Unix_time" id="time_is_link" rel="nofollow" style="font-size:16px">Moscow time. Click for Unix:</a>
    <span id="MSK_z71d" style="font-size:36px"></span>
    <script src="//widget.time.is/t.js"></script>
    <script>
    time_is_widget.init({MSK_z71d:{}});
    </script>

### "Начало эпохи"

**Модуль `time` используется для решения задач, связанных со временем.** Время в компьютере хранится как сумма секунд, которые прошли с [начала эпохи]((https://ru.wikipedia.org/wiki/Unix-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)). Результат на всех Unix-подобных системах будет _1 января 1970 года 00:00_. Эта дата связана с написанием первой официальной версии [операционной системы UNIX](https://ru.wikipedia.org/wiki/Unix).

```Python
import time

## функция для проверки даты начала эпохи
print(time.gmtime(0))

## Ответ: 
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

## сколько секунд прошло с начала эпохи
print(time.time()) # float
```

### Функция sleep

В модуле time есть несколько удобных функций. Одина из них — "уснуть" на указанное количество секунд. В данном случае бесконечно вызывается функция `hello()` в цикле `while`, но интерпретатор ждет 3 секунды и начинает заново.

```Python
import time
## вывод каждый 3 секунд
def hello():
    print('Привет')

while True:
    hello()
    time.sleep(3)
```

!!! danger "Как прервать исполнение кода?"

    Нажмите `Ctrl + C`, чтобы прекратить!

### Замер времени monotonic

В случае, если вам надо измерить время работы части кода, можно воспользоваться функцией monotonic(). • Его главной особенностью является то, что он не может идти назад, если например ОС обновила через интернет свои часы для синхронизации. Функция time в свою очередь спрашивает время в момент запроса (пользовательское время).

```Python
import time

## Замеряем время выполнения вычисления
start = time.monotonic()

## Сложное вычисление
number = 2 ** 100000000

## Считаем разницу текущего времени и начала отсчета
elapsed = time.monotonic() - start
print(f'потрачено {elapsed} секунд')
```

## Модуль datetime

### Объект даты date

**Модуль `datetime` содержит инструменты для работы с форматами даты и времени**. Поддерживаются как стандартные способы представления времени, так и способы более удобные для работы с датами и временными интервалами. Объект `date` хранит значения года, месяца и дня, которые являются обязательными параметрами для создания

```Python
import datetime

## объект date для манипуляций с датами
python_birthday = datetime.date(year=1991, month=2, day=20)
print(python_birthday) # без информации о времени
```

Объект даты `date` позволяет обращаться к отдельным своим составляющим.

```Python
import datetime

python_birthday = datetime.date(year=1991, month=2, day=20)

print(datetime.date.today())  # сегодня
print(python_birthday.year)  # 1991 - тип 'int'
print(python_birthday.month)  # 2
print(python_birthday.day)  # 20
print(python_birthday.weekday())  # 2 – это среда (нумерация с нуля)
```

### Объект времени time

Для обработки только времени можно использовать объект `time`. Также как c `date`, можно обратиться к отдельным частям time.

```Python
import datetime

lunch_time = datetime.time(hour=12, minute=15, second=30, microsecond=5005)

print(f'Время обеда {lunch_time}')
print(lunch_time.hour) # 12 часов
print(lunch_time.minute) # 10 минут
print(lunch_time.second) # 30 секунд
print(lunch_time.microsecond) # 5005 микросекунд
```

Для создания объекта `time` не обязательно указывать все поля. Достаточно одного или двух.

```Python
import datetime

monday_lunch_time = datetime.time(hour=12, minute=15, second=30)
tuesday_lunch_time = datetime.time(hour=12, minute=15)
wednesday_lunch_time = datetime.time(hour=12)

print(
    'Время обеда:', 
    f'понедельник {monday_lunch_time}',
    f'вторник {tuesday_lunch_time}',
    f'среда {wednesday_lunch_time}',
)
```

### Дата и время datetime

А что если нам нужно учитывать как дату, так и время? Для этого есть класс `datetime.datetime`. **Для создания объекта `datetime` обязательно должны учитываться параметры `year`, `month` и `day`.**

```Python
import datetime

fifth = datetime.datetime(year=2005, month=5, day=15, hour=5, minute=50,second=50)

print(f'Что произошло в {fifth}?')
print(datetime.datetime.now()) # сегодня
```

### Форматирование времени

Для того, чтобы **отобразить время в другом формате существует метод `strftime()`**. Правила форматирования задаются с помощью строки, содержащей специальные символы, которые выделены знаком `%`. Вместо них, в зависимости от буквы, будет выведена та, или иная часть даты. При форматировании можно использовать любые символы; обработаны будут только символы с процентом.

В примере:

* `%d` заменяется на 15 - номер дня в месяце,
* `%m` на 05 - номер самого месяца,
* `%Y` на 2005 – год.

```Python
import datetime

fifth = datetime.datetime(year=2005, month=5, day=15, hour=5, minute=50, second=50)

print(fifth.strftime("Момент, когда все оканчивается на пять: %d.%m.%Y"))
print(f'... в момент времени {fifth.strftime("%H:%M:%S")}')
```

Обратная операция для метода strftime — это `strptime()`. **Восстанавливает стандартный объект datetime из форматированной даты в виде строки**.

```Python
new_date = datetime.datetime.strptime('15.05.2005', '%d.%m.%Y')
print(new_date)
```

Метод `combine` можно использовать для объединения идентичных объектов времени.

```Python
print(datetime.datetime.combine(new_date, lunch_time))
```

Время можно вычитать. Результат вычислений будет принадлежать новому классу `timedelta`. Этот класс используется, как отрезок времени, который можно сложить с датой или умножить на константу. [Подробнее по ссылке](https://sky.pro/wiki/python/preobrazovanie-timedelta-v-sekundy-v-python-uchet-dney/).

```Python
new_date -= datetime.datetime(year=1980, month=1, day=1)
print('Разница в днях', new_date, type(new_date))
```

### Задача №5. Ограниченное время

**Условие задачи**

На вашем сайте создали страницу для регистрации пользователей на предстоящую конференцию. Регистрация должна состояться до определенной даты – _1 сентября 2023_. Необходимо проверить дату регистрации участника и сверить эту дату с заданной датой окончания регистрации.

```Python
incoming_date = '02-09-2023' # формат даты в РФ - день, месяц, год
```

??? success "Решение"

    ```Python
    import datetime

    # Формат даты в РФ - день, месяц, год
    incoming_date = '02-09-2023'
    incoming_date_datetime = datetime.datetime.strptime(incoming_date, '%d-%m-%Y')

    ## Создадим дату завершения регистрации
    registration_end_time = datetime.datetime(year=2023, month=9, day=1)

    ## Проверим дату в условии
    if incoming_date_datetime > registration_end_time:
        print('Отказ в регистрации')
    else:
        print('Регистрация одобрена')
    ```

## Промежуточные итоги

* Модуль time и datetime позволяет формировать объекты времени в Python.