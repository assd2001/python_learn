class myStack():
    def __init__(self):
        self.items=[]

    def isempty(self):
        return len(self.items)==0

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isempty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = myStack()
s.push(4)
s.push('cat')
s.pop()
print s.size()