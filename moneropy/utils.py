import sys
from binascii import hexlify
from binascii import unhexlify
from . import ed25519

PYTHON_VERSION = sys.version_info.major

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
