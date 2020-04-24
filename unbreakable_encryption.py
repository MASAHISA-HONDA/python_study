from secrets import token_bytes
from typing import Tuple

def random_key(length:int) -> int:
    #length長のランダムバイトを作成
    tb: bytes = token_bytes(length)
    #int.from_bytes :与えられたバイト列の整数表現を返します。
    #"big"とすることでbyte列の最上位を先頭におく
    return int.from_bytes(tb, "big")

def encrypt(original:str) -> Tuple[int,int]:
    original_bytes = original.encode()
    dummy:int =random_key(len(original_bytes))
    original_key:int = int.from_bytes(original_bytes,"big")
    #XOR処理
    encripted:int = original_key ^ dummy
    return dummy, encripted

def decrypt(key1:int , key2:int) -> str :
    decrypted:int = key1 ^ key2
    #int.to_bytes :与えられた整数のbytes表現を返します。
    temp :bytes = decrypted.to_bytes((decrypted.bit_length()+7) // 8,"big")
    return temp.decode()

if __name__ == "__main__":
    key1,key2 = encrypt("One time Pad!")
    result: str = decrypt(key1,key2)
    print(result)
