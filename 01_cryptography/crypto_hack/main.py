from Crypto.Util.number import *
import base64
from pwn import *


def ascii_decrypt():
    list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    message = ''
    for value in list:
        message += chr(value)
    print(message)


def hex_decrypt():
    str = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
    print(bytes.fromhex(str))

def base64_decrypt():
    hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
    bytes_string = bytes.fromhex(hex_string)
    print(base64.b64encode(bytes_string))

def big_integers_decrypt():
    big_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    bytes = long_to_bytes(big_integer)
    print(str(bytes))

def xor_decrypt():
    s = 'label'
    bytes = bytearray(s, encoding='utf-8')
    msg = []
    for elem in bytes:
        msg.append(xor(elem, 13))
   


def main():
    ascii_decrypt()
    hex_decrypt()
    base64_decrypt()
    big_integers_decrypt()
    xor_decrypt()

if __name__ == "__main__":
    main()