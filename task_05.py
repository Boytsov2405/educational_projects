import datetime

def date_in_future(_date):
    _current_date = datetime.datetime.now().replace(microsecond=0)
    if(not isinstance(_date, int)):
            return _current_date.strftime("%d-%m-%Y %H:%M:%S")
    _future_date = _current_date + datetime.timedelta(days=_date)
    return _future_date.strftime("%d-%m-%Y %H:%M:%S")
    
print(date_in_future([])) # => текущая дата
print(date_in_future(5))
print(date_in_future("ff"))
print(date_in_future(2.5))
print(date_in_future(2)) # => текущая дата + 2 дня
print(isinstance(date_in_future(2), str))