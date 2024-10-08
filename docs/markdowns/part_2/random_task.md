# Обработка случайных значений. Модуль random

## Модуль random и псевдослучайные числа

**Модуль `random` используют для генерации псевдослучайных чисел**. Функции пакета random генерируют случайные значения на основе «зерна» — исходного параметра для генерации случайного значения, например, на основе системное время в миллисекундах.

Для генерации случайного числа int в заданном диапазоне, можно использовать `randint`. А для генерации случайных чисел float — `uniform`.

```Python
import random

## randint выбирает int из диапазона
print(random.randint(0, 10))

## uniform выбирает float из диапазона
print(random.uniform(0.2, 7.5))
```

## Случайность в списках

Значения в созданном списке можно перемешать с помощью `shuffle`. Из списка можно выбрать случайное значение с помощью функции `choice`.Функции `sample` и `choices` выбирают несколько значений. Однако `sample` выбирает значения без повторений, а `choices` выбирает значения с повторами.

```Python
import random

## объявление списка
primes = list(range(50))

## перемешаем список
random.shuffle(primes)
print(primes)

## выбрать одно значение
print(random.choice(primes))

## выбрать несколько значений
print(random.choices(primes, k=3))
print(random.sample(primes, k=3))
```

## Задача №3. Поиск совпадений

**Условие задачи**

Внимательно прочтите условие задачи и скопируйте в среду разработки.

```Python
## а. сгенерируйте последовательность трехзначных чисел от 100 до 1000
## б. выберите 100 случайных значений
## в. при разных способах выборки будет ли различаться количество уникальных значений?
```

Примечание:

* Воспользуйтесь генератором числовых последовательностей.
* Сравните две выборки, которые можно получить с помощью `sample` и `choices`.

??? success "Решение"

    ```Python
    import random

    ## Генерируем последовательность трехзначных чисел
    ids_all = range(100, 1000)

    ## Делаем две выборки с помощью sample и choices
    fids = random.choices(ids_all, k=100)
    sids = random.sample(ids_all, 100)

    ## Проверяем количество уникальных значений в выборке
    print(len(set(fids)))
    print(len(set(sids)))
    ```

## Задача №4. Игральный кубик

**Условие задачи**

Внимательно прочтите условие задачи и скопируйте в среду разработки.

```Python
## Написать скрипт, где игральный кубик (6 сторонний) бросается 4 раза.
## Вывести в результаты каждое выпавшее значение.
## Найти сумму выпавших значений.
```

Примечание:

* Создайте функцию, которая принимает количество бросаний.
* Для генерации числа воспользуйтесь функцией `randint`.

??? success "Решение"

    ```Python
    import random

    ## Создаем функцию для выбора k-случайных значений кубика
    def dice(k):
        values = []
        while k !=0:
            x = random.randint(1, 6)
            k -= 1
            values.append(x)
        return values

    res = dice(4)
    print(res, sum(res))
    ```

## Промежуточные итоги

* Модуль random генерирует случайные числа.