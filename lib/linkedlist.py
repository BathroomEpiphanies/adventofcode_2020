class linkedlist():
    class item():
        def __init__(self,value):
            self.value = value
            self.pred = None
            self.succ = None
        def __str__(self):
            return f'{self.value}'
        def __repr__(self):
            return str(self)
    
    def __init__(self,values,pointer=None):
        self.items = None
        self.first = None
        self.last  = None
        self.pointer = None
        if values:
            self.items = {value:linkedlist.item(value) for value in values}
            for i,_ in enumerate(values):
                self.items[values[i]].succ = self.items[values[(i+1)%len(values)]]
                self.items[values[i]].pred = self.items[values[(i-1)%len(values)]]
            
            self.first = self.items[values[0]]
            self.last  = self.items[values[-1]]
            self.pointer = self.first
    
    def insert(self,sublist,after):
        after = self.items[after]
        
        self.items.update(sublist.items)
        before = after.succ
        after.succ = sublist.first
        sublist.first.pred = after
        before.pred = sublist.last
        sublist.last.succ = before
    
    def remove(self,after,count):
        after = self.items[after]
        first = after.succ
        before = first
        for _ in range(count):
            before = before.succ
        last = before.pred
        after.succ = before
        before.pred = after
        #print(first,last,after,before)
        new = linkedlist([])
        new.first = first
        new.last = last
        new.first.pred = new.last
        new.last.succ = new.first
        new.pointer = new.first
        new.items = self.items
        return new

    
    def __str__(self):
        current = self.first
        out = [f'({current.value})'] if current==self.pointer else [f'{current.value}']
        while True:
            current = current.succ
            if current==self.first: break
            out.append(f'({current.value})' if current==self.pointer else f'{current.value}')
        return ' '.join(out) #+f' {self.items}'


def main():
    test = linkedlist([2,3,4,5])
    print(test)
    test.insert(linkedlist([7,8,9]),after=4)
    print(test)
    sub = test.remove(3,3)
    print(sub)
    print(test)


if __name__ == '__main__': main()
