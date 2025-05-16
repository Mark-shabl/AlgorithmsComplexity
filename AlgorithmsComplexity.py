class AlgorithmsComplexity:
    @staticmethod
    def find_min_max(arr):
        """Поиск минимального и максимального элементов в массиве. Сложность: O(n)"""
        if not arr:
            return None, None
        min_val = max_val = arr[0]
        for num in arr[1:]:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        return min_val, max_val

    @staticmethod
    def fib_recursive(n):
        """Число Фибоначчи (рекурсия). Сложность: O(2^n)"""
        if n <= 1:
            return n
        return AlgorithmsComplexity.fib_recursive(n - 1) + AlgorithmsComplexity.fib_recursive(n - 2)

    @staticmethod
    def fib_iterative(n):
        """Число Фибоначчи (итерация). Сложность: O(n)"""
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    @staticmethod
    def fast_pow(a, b):
        """Быстрое возведение в степень (рекурсия). Сложность: O(log b)"""
        if b == 0:
            return 1
        if b % 2 == 1:
            return a * AlgorithmsComplexity.fast_pow(a, b - 1)
        else:
            temp = AlgorithmsComplexity.fast_pow(a, b // 2)
            return temp * temp

    @staticmethod
    def gcd_euclid(a, b):
        """Алгоритм Евклида для НОД. Сложность: O(log(min(a, b)))"""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def gcd_naive(a, b):
        """Наивный метод для НОД. Сложность: O(min(a, b))"""
        min_num = min(a, b)
        for i in range(min_num, 0, -1):
            if a % i == 0 and b % i == 0:
                return i

    @staticmethod
    def primes_up_to_n(n):
        """Поиск простых чисел до N. Сложность: O(n√n)"""
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes

    @staticmethod
    def longest_increasing_subsequence(arr):
        """Наибольшая возрастающая подпоследовательность. Сложность: O(n^2)"""
        if not arr:
            return 0
        dp = [1] * len(arr)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    @staticmethod
    def quicksort(arr):
        """Быстрая сортировка. Сложность: O(n log n) в среднем, O(n^2) в худшем"""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return AlgorithmsComplexity.quicksort(left) + middle + AlgorithmsComplexity.quicksort(right)

    @staticmethod
    def factorial_recursive(n):
        """Факториал (рекурсия). Сложность: O(n)"""
        return 1 if n <= 1 else n * AlgorithmsComplexity.factorial_recursive(n - 1)

    @staticmethod
    def factorial_iterative(n):
        """Факториал (итерация). Сложность: O(n)"""
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    @staticmethod
    def sieve_of_eratosthenes(n):
        """Решето Эратосфена. Сложность: O(n log log n)"""
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for current in range(2, int(n ** 0.5) + 1):
            if sieve[current]:
                sieve[current * current:: current] = [False] * len(sieve[current * current:: current])
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    @staticmethod
    def count_unique(arr):
        """Подсчет уникальных элементов (с использованием set). Сложность: O(n)"""
        return len(set(arr))

    @staticmethod
    def count_unique_manual(arr):
        """Подсчет уникальных элементов (без set). Сложность: O(n^2) в худшем случае"""
        unique = []
        for item in arr:
            if item not in unique:
                unique.append(item)
        return len(unique)

    @staticmethod
    def is_palindrome(s):
        """Проверка на палиндром. Сложность: O(n)"""
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]


# Пример использования
if __name__ == "__main__":
    ac = AlgorithmsComplexity()

    # Примеры вызовов методов
    print("Минимальный и максимальный элементы:", ac.find_min_max([3, 1, 4, 1, 5, 9, 2, 6]))
    print("10-е число Фибоначчи (рекурсия):", ac.fib_recursive(10))
    print("10-е число Фибоначчи (итерация):", ac.fib_iterative(10))
    print("2^10 (быстрое возведение):", ac.fast_pow(2, 10))
    print("НОД(48, 18) (Евклид):", ac.gcd_euclid(48, 18))
    print("Простые числа до 30:", ac.primes_up_to_n(30))
    print("Длина наибольшей возрастающей подпоследовательности:",
          ac.longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
    print("Отсортированный массив:", ac.quicksort([3, 1, 4, 1, 5, 9, 2, 6]))
    print("5! (рекурсия):", ac.factorial_recursive(5))
    print("5! (итерация):", ac.factorial_iterative(5))
    print("Простые числа до 50 (решето):", ac.sieve_of_eratosthenes(50))
    print("Количество уникальных элементов:", ac.count_unique([1, 2, 2, 3, 4, 4, 5]))
    print("Является ли 'A man, a plan, a canal: Panama' палиндромом?",
          ac.is_palindrome("A man, a plan, a canal: Panama"))