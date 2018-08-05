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

    def _is_emmpy(self):
        return self.head is None or self.tail is None or self.tail == self.head

    def __len__(self):
        if self.head is None or self.tail is None or self.head == self.tail:
            return 0
        elif self.head > self.tail:
            return self.head - self.tail
        else:
            return self.head + (self.size - self.tail)

    def __str__(self):
        if self._is_emmpy():
            return str([])
        elif self.head > self.tail:
            return str(self.data[self.tail:self.head])
        elif self.head < self.tail:
            return str(self.data[self.tail:] + self.data[:self.head])

    def __repr__(self):
        if self.head is None or self.tail is None:
            r = repr([])
        elif self.head >= self.tail:
            r = repr(self.data[self.tail:self.head+1])
        elif self.head < self.tail:
            r = repr(self.data[self.tail:] + self.data[:self.head])
        return "{}:{} {}".format(self.tail, self.head, r)


    def put(self, value):
        # вычисляем и сохраняем следующий индекс, так как в большинстве случаев переполнение буфера не ожидается.
        if self.head is None:
            self.head = self.tail = 0
            self.data[self.head] = value
            return

        next_ptr = (self.head + 1) % self.size
        if next_ptr == self.tail:
            # голова не может наступить на хвост
            raise ValueError("Queue is full.")
        self.head = next_ptr
        self.data[self.head] = value

    def get(self):
        if len(self) == 0:
            raise ValueError("Queue is empty.")
        result = self.data[self.tail]
        self.tail = (self.tail + 1) % self.size
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

if __name__ == "__main__":

    q1 = Queue1(3); q1.prn_state()
    try:
        q1.put(0); q1.prn_state()
        print(q1.get()); q1.prn_state()
    #     q1.put(1); q1.prn_state()
    #     q1.put(2); print(len(q1),repr(q1))
    #     q1.put(3); print(len(q1),repr(q1))
    #     q1.put(4); print(len(q1),repr(q1))
    except ValueError as e:
        print(e)
    #
    # print(q1.data)
    #
    # print(q1.get(), repr(q1), q1.data)
    # print(q1.get(), repr(q1), q1.data)
    # print(q1.get(), repr(q1), q1.data)

