#Modificar el iterador de fibonacci, para que en lugar de devolver los infinitos números, solo devuelva
#los números hasta un máximo. Una vez que esto pase , eleva un error StopIteration

import time

class FiboIter():
    def __init__(self, max = None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.n2 <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration
        
if __name__ == '__main__':
    fibonacci = FiboIter(4)
    for element in fibonacci:
        print(element)
        time.sleep(1)