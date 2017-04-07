# MoneroPy - A python toolbox for Monero
# Copyright (C) 2016 The MoneroPy Developers.
#
# MoneroPy is released under the BSD 3-Clause license. Use and redistribution of
# this software is subject to the license terms in the LICENSE file found in the
# top-level directory of this distribution.

from binascii import hexlify, unhexlify
from .crypto import ed25519
from . import utils
#from .crypto.Keccak import Keccak
import sys
import sha3

b = ed25519.b
q = ed25519.q
l = ed25519.l

_hexStrToInt = utils.hexStrToInt
_intToHexStr = utils.intToHexStr

def cn_fast_hash(s):
    return keccak_256(unhexlify(s))

def keccak_256(s):
    #return Keccak().Keccak((len(s)*4, s), 1088, 512, 0x01, 32*8, False).lower()
    k = sha3.keccak_256()
    k.update(s)
    return k.hexdigest()

def sc_reduce(key):
    return _intToHexStr(_hexStrToInt(key) % l)

def sc_reduce32(key):
    return _intToHexStr(_hexStrToInt(key) % q)

def public_from_int(i):
    pubkey = ed25519.encodepoint(ed25519.scalarmultbase(i))
    return hexlify(pubkey)

def public_from_secret(sk):
    return public_from_int(_hexStrToInt(sk)).decode('utf-8')

scalarmult_base = public_from_secret
