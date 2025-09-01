import re
class BlockTranspositionCipher:
    LATTERS = "abcdefghijklmnopqrstuvwxyz"
    def __init__(self, _text, _key, decrypt = False):
        self._key_latters_list = []
        self._en_de_crypted_text = []
        self._counter_iter = 0
        self.key = _key  
        self.decrypt = decrypt
        self.text = _text 
        
    @property
    def decrypt(self):
        return self._decrypt
    @decrypt.setter        
    def decrypt(self,_val:bool):  
        if(isinstance(_val, bool)):
            self._decrypt = _val
        else:
            raise ValueError("Decrypt must be a bool.")   
    def __iter__(self):
        self._counter_iter = 0
        return self
    def __next__(self):
        if(self._counter_iter > len(self._en_de_crypted_text)-1):
            raise StopIteration
        _curr_text = self._en_de_crypted_text[self._counter_iter]
        self._counter_iter+=1
        return _curr_text
        
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self,_val:str):
        if(isinstance(_val, str)):
            if(self.decrypt):
                self.decrypt_text(_val)
            else:
                self.encrypt_text(_val)    
        else:
            raise ValueError("Text must be a str.")   
    def encrypt_text(self, _val):
        _block_size = len(self.key)
        _blocks = [_val[i:i+_block_size] for i in range(0, len(_val), _block_size)]
        if len(_blocks[-1]) < _block_size:
            _blocks[-1] = _blocks[-1] + " " * (_block_size - len(_blocks[-1]))
        for _word_ind in range(len(_blocks)):
            _word_start = [i for i in _blocks[_word_ind]]
            _word_end = [i for i in _blocks[_word_ind]]
            for _k in range(_block_size):
                _word_end[_k] = _word_start[self._key_latters_list[_k]]
            _blocks[_word_ind] = "".join(_word_end)

        self._en_de_crypted_text = _blocks
        self._text = _val    
    def decrypt_text(self, _val):
        _block_size = len(self.key)
        _blocks = [_val[i:i+_block_size] for i in range(0, len(_val), _block_size)]
        if len(_blocks[-1]) < _block_size:
            _blocks[-1] = _blocks[-1] + " " * (_block_size - len(_blocks[-1]))
        for _word_ind in range(len(_blocks)):
            _word_start = [i for i in _blocks[_word_ind]]
            _word_end = [i for i in _blocks[_word_ind]]
            for _k in range(_block_size):
                _word_end[self._key_latters_list[_k]] = _word_start[_k]
            _blocks[_word_ind] = "".join(_word_end)
       
        self._en_de_crypted_text = _blocks#"".join(_blocks)
        self._en_de_crypted_text[-1] = self._en_de_crypted_text[-1].rstrip() 
        self._text = _val    
   
    @property
    def key(self):
        return self._key
    @key.setter
    def key(self,_val:str):
        if(isinstance(_val, str)):
            if(len(set(_val.lower())) == len(_val.lower())):
                if(re.fullmatch("[a-zA-Z]+",_val) is not None):
                    _key_indices = [self.LATTERS.index(ch) for ch in _val.lower()]
                    _sorted_indices = sorted(_key_indices)
                    self._key_latters_list = [_sorted_indices.index(_k) for _k in _key_indices]
                    self._key = _val
                else:
                    raise ValueError("Key must contain only latin letters.")
            
            else:
                raise ValueError("Key must contain only unique letters.")
        else:
            raise ValueError("Key must be a str.")
           
            
            
text = "CODE WITH PYTHON!"
key = "dacb"
cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")
#Пример 4: Полное дешифрование с обрезкой пробелов
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'\n")   
print("---------------------------------------------")   

text = "HELLO"
key = "bac"
cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")
#Пример 4: Полное дешифрование с обрезкой пробелов
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'\n")   


            
text = 33
key = []
cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")
#Пример 4: Полное дешифрование с обрезкой пробелов
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'\n")   
print("---------------------------------------------")    