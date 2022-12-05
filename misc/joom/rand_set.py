# // Спроектировать структуру, позволяющую за амортизированную O(1) выполнять операции:
# // a) равновероятное получение случайного элемента среди содержимого
# // б) добавление/удаление элемента по значению (как HashSet)

# // Описание интерфейса для удобства:
# // RandSet collection with complexity O(1) for all operations
# // type RandSet interface {
# //     Add(v int) 
# //     Remove(v int)
# //     Rand() int
# // }

import random

# Rand()
# None
# Add(1)
# values: [1]; hashmap: {1: i=0}
# Rand()
# rand: 0; return: 1
# Add(2)
# values: [1, 2]; hashmap: {1: i=0; 2: i=1}
# Rand()
# rand=1; return: 2
# Remove(1)
# rm_i: 0; curr_last: 2 (values: [1]); put 2 by rm_i=0 => values: [2]; hash[2]=0 .... hashmap: {2: i=0}
# Rand()
# ...

class RandSet():
    def __init__(self):
        self.hashmap = {}
        self.values = []
        
    def Add(v):
        if v not in self.hashmap:
            return
        self.values.append(v)    
        self.hashmap[v] = len(self.values) - 1
    
    def Remove(v):
        if v not in self.hashmap:
            return
        
        # update values
        rm_i = self.hashmap[v]
        curr_last_value = self.values.pop()
        self.values[rm_i] = curr_last_value
        # update hashmap
        self.hashmap[curr_last_value] = rm_i
        
        del self.hashmap[v]

    def Rand():
        if not self.values:
            return None

        i = random.randint(len(self.values) - 1)
        return self.values[i]