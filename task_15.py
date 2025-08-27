import re
class BlockTranspositionCipher:
    LATTERS = "abcdefghijklmnopqrstuvwxyz"
    def __init__(self, _text, _key, decrypt = False):
        self._key_latters_list = []
        self._en_de_crypted_text = []
        self.key = _key
        self.text = _text
        self._counter_iter  = 0
        self.decrypt = decrypt
        
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
                self.decrypt(_val)
            else:
                self.encrypt(_val)    
        else:
            raise ValueError("Text must be a str.")   
    def encrypt(self, _val):
        _block_size = len(self.key)
        _encrypted_text_tmp = [_val[_i:_i +_block_size] for _i in range(0, len(_val), _block_size)]
        if(len(_encrypted_text_tmp[-1])<_block_size):
            _encrypted_text_tmp[-1] = _encrypted_text_tmp[-1]+" "*(_block_size-len(_encrypted_text_tmp[-1]))
        self._en_de_crypted_text = ["".join(_encrypted_part[_ord] for _ord in self._key_latters_list) for _encrypted_part in _encrypted_text_tmp]    
        self._text = _val        
    def decrypt(self, _val):
        _block_size = len(self.key)
        _decrypted_text_tmp = [_val[_i:_i +_block_size] for _i in range(0, len(_val), _block_size)]
        if(len(_decrypted_text_tmp[-1])<_block_size):
            _decrypted_text_tmp[-1] = _decrypted_text_tmp[-1]+" "*(_block_size-len(_decrypted_text_tmp[-1]))
        for _decrypted_part in _decrypted_text_tmp:
            _part_tmp = [_latter for _latter in _decrypted_part] 
            for _i in range(_block_size):
                _part_tmp[_i] = _decrypted_part[self._key_latters_list[_i]]
            self._en_de_crypted_text.append("".join(_part_tmp))
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
                    _key_latters_list_tmp = [self.LATTERS.index(_key_latter) for _key_latter in _val.lower()]
                    _sorted_list = sorted(_key_latters_list_tmp)
                    self._key_latters_list = [_key_latters_list_tmp.index(_ind) for _ind in _sorted_list]
                    self._key = _val
                else:
                    raise ValueError("Key must contain only latin letters.")
            
            else:
                raise ValueError("Key must contain only unique letter.")
        else:
            raise ValueError("Key must be a str.")   
            
#Пример 1: Шифрование с явной итерацией по блокам
text = "HELLOWORLD"
key = "bAc"
print("Процесс шифрования по блокам:")
cipher = BlockTranspositionCipher(text, key)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

#Пример 2: Полное шифрование
cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")

print("\nПроцесс дешифрования по блокам:")
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
for i, decrypted_block in enumerate(decipher, 1):
    print(f"Блок {i}: '{decrypted_block}'")
#Пример 4: Полное дешифрование с обрезкой пробелов
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'")    
