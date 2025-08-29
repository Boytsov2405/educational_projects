import re

def count_words(_sentence:str) -> dict:
    _words = [
        re.sub(r"[^\w]", "", _word).lower()
        for _word in _sentence.split()
        if re.sub(r"[^\w]", "", _word).isalpha()
    ]
    _uniq = set(_words)
    _result = {_word: _words.count(_word) for _word in _uniq}
    return dict(sorted(_result.items(), key = lambda _item:_item[1],reverse = True))


print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}