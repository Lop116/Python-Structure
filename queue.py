class queue:
    def __init__(self,limit):
        self.items = [None] * limit
        self.frontpointer = 0
        self.rearpointer = -1
        self.queuelenght = 0 
        self.queuefull = limit 

    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
        else:
            if self.rearpointer == (self.queuefull - 1):
                self.rearpointer = - 1
            self.rearpointer +=1
            self.queuelenght +=1
            self.items[self.rearpointer] = data
            print("Data was entered")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.queuelenght -=1
            self.items[self.frontpointer] = None
            if self.frontpointer == (self.queuefull - 1):
                self.frontpointer = 0
            else:
                self.frontpointer +=1
            print("Data was deleted")

    def front(self):
        return self.items[self.frontpointer]

    def is_empty(self):
        if self.queuelenght == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.queuelenght == self.queuefull:
            return True
        else:
            return False

    def size(self):
        return self.queuelenght

    def display(self):
        count = self.frontpointer
        for i in range(0, self.queuelenght):
            print(self.items[count], end = " ")
            if count == (self.queuefull - 1):
                count = 0
            else:
                count += 1
            