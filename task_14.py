class EvenNumbers:
    def __init__(self, _num):
        if(isinstance(_num, int)):
            self._counter_iter = 0;
            self._num_list = [_i*2 for _i in range(_num)]
        else:
            raise TypeError("_num must be an int.")
    def __iter__(self):
        return self
    def __next__(self):
        if(self._counter_iter > len(self._num_list)-1):
            raise StopIteration
        _curr_num = self._num_list[self._counter_iter]
        self._counter_iter+=1
        return _curr_num
        
evens = EvenNumbers(5)
for num in evens:
    print(num) # Должно вывести 0, 2, 4, 6, 8
for num in evens:
    print(num) # Должно вывести 0, 2, 4, 6, 8