class Convergence():
    """
    Реализация генератора простых чисел с кэшированием уже вычисленных значений.
    """

    def __new__(cls, *args):
        """ for Singletone """
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args)
        return cls._instance

    def __init__(self, num=2):
        """
        Конструктор может сразу создать необходимиое количество простых чисел в кеше.
        :param num: максимально ожидаемое число позволяет сразу закешировать весь ряд простых числе до >= num
        """
        self.clear()
        self.is_prime(num)

    def clear(self):
        self.primes = [2, ]

    def is_prime(self, num):
        """
        Проверка на вхождение в ряд простых чисел.
        Также выполняется кеширование всего ряда до >= num

        :param num: проверяемое число позволяет сразу закешировать весь ряд простых числе до >= num
        :return:
        """
        if num < 1:
            return False
        elif num == 1:
            return True
        elif num <= self.primes[-1]:
            return num in self.primes

        # Заполнить кеш значениями простых чисел до >= искомого
        for i in range(self.primes[-1]+1, num+1):  # генерируем кандидатов на простое число
            for j in self.primes:   # проверяем делители из кэша простых чисел
                if i % j == 0:
                    # если i делится на одно из простых числел, то дальше проверять нет смысла
                    # и надо перейти к следующему кандидату
                    break
            else:
                # если не разделилось ни на одно из простых числел, то надо дописать в кеш
                self.primes.append(i)

        return num == self.primes[-1]
