def coincidence(_list:list = None, _range:range = None) -> list:
    if(_list is None or _range is None): return [];
    return [_num for _num in _list if isinstance(_num, (int, float)) and _range.start<= _num <_range.stop]
 

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))