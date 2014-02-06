import array
import random

# Although this specific Queue class has bugs spread
# throughout the code, do not modify the class.
class Queue:

    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max - 1
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        x = x % 1000
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self
                    .size==0) or (self.size==self.max)


def random_test():
    results_list = []
    que = Queue(500)
    for i in range(10000):
        random_num = random.randrange(1,1000)
        if random.random() > 0.5:
            que.enqueue(random_num)
            try:
                que.checkRep()
                results_list.append((random_num, 0))
            except Exception:
                results_list.append((random_num, 1))
        else:
            que.dequeue()
            try:
                que.checkRep()
                results_list.append(('dq', 0))
            except Exception:
                results_list.append(('dq', 1))


    return results_list

random_test()

