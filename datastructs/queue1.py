#!/usr/bin/env python3

class Queue1:
    """ Реализация структуры данный Однонаправленная Очередь FIFO с фиксированным размером"""
    def __init__(self, size=2):
        if size < 2:
            raise ValueError("Size of Queue1 must be more then 1.")
        self.size = size
        self.data = [None for x in range(self.size)]
        self.head = None    # позиция, в которую будет сделана следующая запись.
        self.tail = None    # позиция, из которой будем считывать.

    def is_emmpy(self):
        """ Очередь пуста только тогда, когда оба указателя сброшены в None """
        return self.head is None or self.tail is None   # or self.tail == self.head

    def __len__(self):
        if self.is_emmpy():
            return 0
        elif self.head > self.tail:
            return self.head - self.tail
        else:  # self.head <= self.tail
            return self.head + (self.size - self.tail)

    def __str__(self):
        """ Только данные в очереди, которые записаны и не вычитаны, т.е. готовы к получению. """
        if self.is_emmpy():
            return str([])
        elif self.head > self.tail:
            return str(self.data[self.tail:self.head])
        elif self.head <= self.tail:
            return str(self.data[self.tail:] + self.data[:self.head])

    def __repr__(self):
        """ Отладочный вывод показывает:
         хвост
         голову
         сырой массив
         """
        return "{}:{} {}".format(repr(self.tail), repr(self.head), repr(self.data))

    def put(self, value):
        # вычисляем и сохраняем следующий индекс, так как в большинстве случаев переполнение буфера не ожидается.
        if self.head is None:
            self.head = self.tail = 0
            self.data[self.head] = value
        elif self.head == self.tail:
            # голова не может наступить на хвост
            raise ValueError("Queue is full.")
        else:
            self.data[self.head] = value
        self.head = (self.head + 1) % self.size
        return

    def get(self):
        if self.is_emmpy():
            raise ValueError("Queue is empty.")
        result = self.data[self.tail]
        self.tail = (self.tail + 1) % self.size
        if self.tail == self.head:
            self.tail = self.head = None
        return result

    def prn_state(self):
        # if self.head  and self.tail: это тот случай, когда нельзя полагаться на приведение типов,
        # так как мы приняли, что в позиции self.data[0] могут храниться данные.
        if self.head is not None and self.tail is not None:
            print(
                "l={0} head={1} tail={2} queue={3} rawdata={4}".format(
                    len(self),
                    self.head,
                    self.tail,
                    str(self),
                    str(self.data),
                )
            )
        else:
            print("Queue is empty!")