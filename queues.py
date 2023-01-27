

class Queue:
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        if self.is_empty():
            return ""
        queue_str = ''
        current = self.queue[0]
        while current:
            queue_str += str(current) + ' -> '
            current = self.queue.pop(0)
        return queue_str[:-4]
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.queue:
            raise QueueUnderflowException("Queue is empty")
        else:
            return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)
    
    
class QueueUnderflowException(Exception):
    pass
