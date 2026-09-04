class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # available spaces
        self.size = 0 # initialize size
        self.arr = [None] * capacity # initialize the value into the index of arrays

    def get(self, i: int) -> int:
        return self.arr[i] 

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if(self.size == self.capacity):
            self.resize()
        self.arr[self.size] = n
        self.size +=1
          

    def popback(self) -> int:
        pop =self.get(self.size -  1)
        self.size -=1
        return pop

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr


    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity
