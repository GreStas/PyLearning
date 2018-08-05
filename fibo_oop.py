#!/usr/bin/env python3

class Fibonachi:
    """ Число Фибоначи с поддержкой обращения по индексу
    Используется шаблон проектирования Singleton для кеширования
    уже посчитанных значений.
    """

    fibos = [1, 1, ]

    def __new__(cls):
        """ for Singletone """
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __getitem__(self, item):
        if item > len(self.fibos):
            # надо добавить в список новые элементы
            for i in range(len(self.fibos), item):
                self.fibos.append(self.fibos[i - 2] + self.fibos[i - 1])
        return self.fibos[item - 1]

    def __len__(self):
        return len(self.fibos)

    def __str__(self):
        return "Fibonachi[{}]={}..{}".format(len(self.fibos), self.fibos[0], self.fibos[-1])

    def __repr__(self):
        return "Fibonachi"+str(self.fibos)


def print_state(name, obj, ind=None):
    if ind:
        print( "{3}[{1} из {2}] = {0}".format(obj[ind], ind, len(obj), name) )
    print("str({0}):\t {1}\nrepr({0}):\t {2}".format(name, str(obj), repr(obj)))


if __name__ == '__main__':

    f1 = Fibonachi()
    print_state('f1', f1)

    print_state('f1', f1, 10)

    print_state('f1', f1, 20)

    print_state('f1', f1, 15)

    print("\nПродемонстрируем, что второй экземпляр класса позволяет использовать уже созданый кэш Синглтона.")

    f2 = Fibonachi()
    print_state('f2', f2, 18)

