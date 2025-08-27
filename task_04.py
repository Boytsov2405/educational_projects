def sort_list(_list:list) -> list:
    if not _list: return _list
    _min = _max = None
    for _el in _list:
        if isinstance(_el, (int, float)):
            if _min is None or _el < _min: _min = _el
            if _max is None or _el > _max: _max = _el
    if(_min == _max): _result = _list;
    else:
        _result = [_max if _el == _min else _min if _el == _max else _el for _el in _list]
    _result.append(_min)
    return _result
print(sort_list(["fff",245]))
print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]