import time

def cached(_func = None, *, max_size = None, seconds = None):
    def real_cached(_func):
        _cache = {}
        _lifetime = {}
        def wrapper(*args, **kwargs):
            _key = (*args, tuple(sorted(kwargs.items())))
            if(seconds is not None):
                if(isinstance(seconds, int) and seconds > 0):
                    for _key_time in list(_lifetime.keys()):
                        if _lifetime[_key_time] <= time.time():
                            del _lifetime[_key_time]
                            del _cache[_key_time]
                    _lifetime[_key] = time.time()+seconds
                else:
                    raise TypeError("seconds must be a positive int")
            if(_key in _cache):
                return _cache[_key]
            _cache[_key] = _func(*args, **kwargs)
            if(max_size is not None):
                if(isinstance(max_size, int) and max_size > 0):
                    if(max_size < len(_cache)):
                        del _cache[(list(_cache.keys()))[0]]
                else:
                    raise TypeError("max_size must be a positive int")
            return  _cache[_key]
            
        return wrapper
    if _func is not None:
        return real_cached(_func)
    return real_cached   
    
@cached(max_size=3, seconds= 10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2
    
# Первый вызов — вычисляется
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(2)) # Вывод: 4 (без вычисления)
# Через 15 секунд кэш устареет, и будет новое вычисление
time.sleep(15)
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4