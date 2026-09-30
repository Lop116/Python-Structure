class stack:
    def __init__(self,limits):
        self.items = []
        self.limits = limits

    def push(self,data): #add value in the stack
        if self.size() < self.limits:
            self.items.append(data)
            print(f'The data {data} was added')
        else:
            print("The stack is full")

    def pop(self): #remove data from the list
        if not self.is_empty():
            print(f'The data {self.items.pop()} was removed')
        else:
            print("The stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[self.size()-1]
        else:
            print("The stack is empty")
        
    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            for i in reversed(self.items):
                print(i, end=" ")
            print(" ")
        else:
            print("The stack is empty")


s = stack(5)
print(f'Size : {s.peek()}')
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.pop()
s.pop()
s.display()
s.push(5)
s.push(6)
print(f'Size : {s.peek()}')
print(f'Size : {s.size()}')