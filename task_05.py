import datetime

def date_in_future(_date):
    _current_date = datetime.datetime.now()
    if(not isinstance(_date, int)):
            return _current_date
    return _current_date + datetime.timedelta(_date)
    
print(date_in_future([])) # => текущая дата
print(date_in_future(5))
print(date_in_future("ff"))
print(date_in_future(2.5))
print(date_in_future(2)) # => текущая дата + 2 дня