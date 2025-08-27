def connect_dicts(_dict1:dict, _dict2:dict) -> dict:
    _MIN_VAL = 10;
    _priority_dict = None;
    _other_dict = None;
    _result_dict = {};
    if(sum(_dict1.values()) <= sum(_dict2.values())):
        _priority_dict = _dict2;
        _other_dict = _dict1;
    else:
        _priority_dict = _dict1;
        _other_dict = _dict2;
    _result_dict = {_key: _val for _key, _val in _priority_dict.items() if _val >= _MIN_VAL}
    _extra_dict = {_key:_val for _key,_val in _other_dict.items() if _val >= _MIN_VAL and not _key in _result_dict}
    _result_dict.update(_extra_dict)
    return dict(sorted(_result_dict.items(), key = lambda _item: _item[1]))
        
print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # =>{ "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # =>{ d: 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # =>{ "c": 11, "b": 12, "a": 15 }