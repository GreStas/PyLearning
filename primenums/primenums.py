class Convergence:
    """
    Реализация проверки на вхождение в ряд простых чисел с кэшированием уже вычисленных значений.
    """

    def __new__(cls, *args, **kwargs):
        """ for Singletone """
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            """ Следующий вариант вызывает ошибку "TypeError: object.__new__() takes no arguments"
                если его использовать в консоле интерпритатора.
                В unittest ошибки нет.
            cls._instance = super().__new__(cls, *args, **kwargs)
            """
        return cls._instance

    def __init__(self, num=2):
        """
        Конструктор может сразу создать необходимиое количество простых чисел в кеше.
        :param num: максимально ожидаемое число позволяет сразу закешировать весь ряд простых числе до >= num
        """
        if not hasattr(self, 'primes'):
            self.clear()
        self.is_prime(num)

    def clear(self):
        self.primes = [2, ]

    def __len__(self):
        return len(self.primes)

    @property
    def get_primes(self):
        return self.primes

    def is_prime(self, num):
        """
        Проверка на вхождение в ряд простых чисел.
        Также выполняется кеширование всего ряда до >= num

        :param num: проверяемое число позволяет сразу закешировать весь ряд простых числе до >= num
        :return:
        """
        if num is None or num < 1:
            return False
        elif num == 1:
            return True
        elif num <= self.primes[-1]:
            return num in self.primes

        # Заполнить кеш значениями простых чисел до >= искомого
        while num > self.append():
            pass

        return num == self.primes[-1]

    def append(self):
        """
        Добавить новый элемент в конец ряда
        :return: Значение добавленного элемента
        """
        i = self.primes[-1] + 1
        while True:
            for j in self.primes:   # проверяем делители из кэша простых чисел
                if i % j == 0:
                    # если i делится на одно из простых числел, то дальше проверять нет смысла
                    # и надо перейти к следующему кандидату
                    i += 1
                    break
            else:
                # если не разделилось ни на одно из простых числел, то надо дописать в кеш и вернуть найденное значение
                self.primes.append(i)
                return i


class Primes:
    """
    Реализация получения простых чисел:
    * по номеру в ряде
    * следующее  значение после указанного
    * генератор последовательности с про-буферизацией на N-элементов вперёд в случае если не попали в кэш
    """
    def __init__(self, bufsize=1):
        self.base = Convergence()
        self.bufsize =  int(bufsize) if bufsize is not None and bufsize > 0 else 1

    @property
    def get_primes(self):
        return self.base.get_primes

    def clear(self):
        self.base.clear()

    def forward(self):
        """
        Сформировать дополнительно buf-элементов
        :param items: размер буфера - количество элементов
        :return: list of appended items
        """
        cur_len = len(self.base.primes)
        for i in range(self.bufsize):
            self.base.append()
        return self.base.primes[cur_len:]

    def __getitem__(self, item):
        while item >= len(self.base):
            self.forward()
        return self.base.primes[item]

    def __len__(self):
        return len(self.base.primes)


class GenPrimes(Primes):

    def __next__(self):
        i = 0
        while True:
            while i < len(self.primes):
                yield self.primes[i]
            self.reward()

    def __call__(self, *args, **kwargs):
        return self.__next__()