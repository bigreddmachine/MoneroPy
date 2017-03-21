import sys as _sys
import os as _os
from binascii import hexlify
from binascii import unhexlify
from .crypto import ed25519 as ed25519
from . import base58 as _b58

PYTHON_VERSION = _sys.version_info.major

if PYTHON_VERSION == 3:
    def hexStrToInt(h):
        '''Converts a hexidecimal string to an integer.'''
        return int.from_bytes(unhexlify(h), "little")

    def intToHexStr(i):
        '''Converts an integer to a hexidecimal string.'''
        return hexlify(i.to_bytes(32, "little")).decode("latin-1")

else:
    def hexStrToInt(h):
        '''Converts a hexidecimal string to an integer.'''
        byt = unhexlify(h)
        return sum((2**i * ed25519.bit(byt, i)) for i in range(0, len(h)*4))

    def intToHexStr(i):
        '''Converts an integer to a hexidecimal string.'''
        return hexlify(ed25519.encodeint(i))

def gen_random_hex(n_bytes=32):
    '''Generate a secure random hexadecimal string.

    By default, this will generate a 32-byte string. However, it can generate a
    string of any byte size by inputing the desired number of bytes.

    Example:
    --------
        h = get_random_hex(8)
    '''
    h = hexlify(_os.urandom(n_bytes))
    return "".join(h.decode("utf-8"))

def gen_payment_id(id_type='normal'):
    '''Generate a 64-bit or 32-byte random hexadecimal payment ID.'''
    if id_type == 'integrated': # 64-bit Payment ID for integrated addresses
        pid = gen_random_hex(8)
    else: # 32-byte regular hexadecimal payment ID
        pid = gen_random_hex(32)
    return pid

def parse_extra_hex(h):
    '''Parse the extra field of a Monero transaction.

    Example:
      pub, pay_id = parse_extra(b)

    Input:
      - h (hex) -- tx extra field

    Outputs:
      - pub (str) -- hexadecimal transaction public key
      - pay_id (str) -- hexadecimal transaction payment id
    '''
    pub = ''
    pay_id = ''
    b = _b58._hexToBin(h)

    if b[0] == 1: # pubkey is tag 1
        pub = h[2:66] # pubkey is 32 bytes # = _b58._binToHex(b[1:33])

        if len(b) >= 66:
            if b[33] == 2 and b[35] == 0 or b[35] == 1:
                pay_id = h[72:(72+b[34]*2-2)] # = _b58._binToHex(b[36:(36+b[34]-1)])

    elif b[0] == 2:
        if b[2] == 0 or b[2] == 1:
            pay_id = h[6:(6+b[1]*2-2)] # = _b58._binToHex(b[3:(3+b[1]+1)]) #

        # second byte of nonce is nonce payload length
        # pubkey tag location: payload length + nonce tag byte + payload length byte
        if b[2+b[1]] == 1:
            offset = (2+b[1]) * 2 # = 2 + b[1]
            pub = h[(offset+2):(offset+2+64)] # = _b58._binToHex(b[(offset+1):(offset+1+32)])

    return pub, pay_id

def parse_extra_bin(b):
    '''Parse the extra field of a Monero transaction.

    Example:
      pub, pay_id = parse_extra(b)

    Input:
      - b (bin) -- tx extra field

    Outputs:
      - pub (str) -- hexadecimal transaction public key
      - pay_id (str) -- hexadecimal transaction payment id
    '''
    pub = ''
    pay_id = ''
    h = _b58._binToHex(b)

    if b[0] == 1: # pubkey is tag 1
        pub = h[2:66] # pubkey is 32 bytes # = _b58._binToHex(b[1:33])

        if len(b) >= 66:
            if b[33] == 2 and b[35] == 0 or b[35] == 1:
                pay_id = h[72:(72+b[34]*2-2)] # = _b58._binToHex(b[36:(36+b[34]-1)])

    elif b[0] == 2:
        if b[2] == 0 or b[2] == 1:
            pay_id = h[6:(6+b[1]*2-2)] # = _b58._binToHex(b[3:(3+b[1]+1)])

        # second byte of nonce is nonce payload length
        # pubkey tag location: payload length + nonce tag byte + payload length byte
        if b[2+b[1]] == 1:
            offset = (2+b[1]) * 2 # = 2 + b[1]
            pub = h[(offset+2):(offset+2+64)] # = _b58._binToHex(b[(offset+1):(offset+1+32)])

    return pub, pay_id
