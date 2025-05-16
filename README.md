
# Algorithms Complexity Analyzer

Этот проект содержит реализацию различных алгоритмов с анализом их временной сложности на Python. Все алгоритмы объединены в класс `AlgorithmsComplexity` для удобного использования.

## Содержание

1. [Установка](#установка)
2. [Использование](#использование)
3. [Список алгоритмов](#список-алгоритмов)
4. [Примеры](#примеры)
5. [Тестирование](#тестирование)
6. [Вклад в проект](#вклад-в-проект)
7. [Лицензия](#лицензия)

## Установка

Для использования этого проекта вам потребуется Python 3.6 или выше.

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/algorithms-complexity.git
cd algorithms-complexity
```

2. (Опционально) Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
venv\Scripts\activate    # для Windows
```

## Использование

Импортируйте класс `AlgorithmsComplexity` и используйте его методы:

```python
from algorithms_complexity import AlgorithmsComplexity

ac = AlgorithmsComplexity()

# Пример использования
min_val, max_val = ac.find_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {min_val}, Max: {max_val}")
```

## Список алгоритмов

1. Поиск минимального и максимального элементов в массиве - O(n)
2. Числа Фибоначчи (рекурсивный и итеративный методы)
3. Быстрое возведение в степень - O(log b)
4. Алгоритм Евклида для НОД - O(log(min(a, b)))
5. Поиск простых чисел до N - O(n√n)
6. Наибольшая возрастающая подпоследовательность - O(n²)
7. Быстрая сортировка - O(n log n) в среднем случае
8. Факториал (рекурсивный и итеративный методы) - O(n)
9. Решето Эратосфена - O(n log log n)
10. Подсчет уникальных элементов - O(n)
11. Проверка строки на палиндром - O(n)

Каждый метод содержит docstring с описанием его временной сложности.

## Примеры

Примеры использования всех методов можно найти в блоке `if __name__ == "__main__":` в файле `algorithms_complexity.py`.

Для запуска примеров выполните:
```bash
python algorithms_complexity.py
```

## Тестирование

Для добавления тестов создайте файл `test_algorithms.py` и используйте unittest или pytest. Пример теста:

```python
import unittest
from algorithms_complexity import AlgorithmsComplexity

class TestAlgorithms(unittest.TestCase):
    def test_find_min_max(self):
        ac = AlgorithmsComplexity()
        self.assertEqual(ac.find_min_max([3, 1, 4, 1, 5]), (1, 5))

if __name__ == "__main__":
    unittest.main()
```

## Лицензия

[MIT](https://choosealicense.com/licenses/mit/)
