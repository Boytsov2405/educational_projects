def max_odd(_list:list) -> int:
    return max((_num for _num in _list if isinstance(_num, (int, float)) and _num%2!=0), default = None)
 

print(max_odd([1, 2, 3, 4, 4])) # => 3
print(max_odd([21.0, 2, 3, 4, 4])) # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu'])) # => None
print(max_odd([2, 2, 4]))# => None