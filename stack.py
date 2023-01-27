
class Stack:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        if self.is_empty():
            return ""
        return ' -> '.join(str(i) for i in self.items[::-1])
    
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.items:
            raise StackPopException
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)
    
    def add(self, item):
        self.push(item)


class StackPopException(Exception):
    pass