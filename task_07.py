def combine_anagrams(_list:list) ->list:
    _sorted_words = {}
    for _word in _list:
        if(isinstance(_word, str)):
            _potential_key = ''.join(sorted(_word.strip().lower()))
            if _potential_key in _sorted_words:
                _sorted_words[_potential_key].append(_word)
            else:
                _sorted_words[_potential_key] = [_word]
            
    return list(_sorted_words.values());
    
print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])) # => [ ["cars", "racs", "scar"], ["four"], ["for"],["potatoes"], ["creams", "scream"] ]