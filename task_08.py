import re

def multiply_numbers(_inputs = None) ->int:
    _result = None
    if(isinstance(_inputs, list)):
        if(len(_inputs) ==0):
            return None
        for _el in _inputs:
            _res_num = multiply_numbers(_el)
            if(_res_num is not None):
                if _result == None: _result = _res_num
                else: _result*=_res_num
    else:
        _inputs = re.findall('-?\\d', str(_inputs).replace(" ",""))
        
        if(len(_inputs)==0):
            return None
        _result = 1
        for _el in _inputs:
            _result*= int(_el)
    return _result
print(multiply_numbers())      
print(multiply_numbers(["FA-5F",-5,"3-3",[3,2]]))   
print(multiply_numbers("FA5F"))
print(multiply_numbers("-2.5"))
print(multiply_numbers("3 - 3"))
print(multiply_numbers(["Fава",["ААВВ"]]))
print(multiply_numbers([]))