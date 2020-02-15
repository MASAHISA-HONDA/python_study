from secreats import token_bytes
from typing import Tuple

def random_key(length:int) -> int:
    #length長のランダムバイトを作成
    td: bytes = token_bytes(length)
    #バイトをビット列にして返す
    #"big"とすることでbyte列の最上位を先頭におく
    return int.from_bytes(tb, "big")

def encrypt(original:str) -> Tuple