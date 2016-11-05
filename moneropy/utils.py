import sys as _sys
import os as _os
from binascii import hexlify
from binascii import unhexlify
from . import ed25519

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

def gen_payment_id():
    '''Generate a 32-byte random hexadecimal string to use as a payment ID.'''
    return gen_random_hex(32)
