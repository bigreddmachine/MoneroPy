# MoneroPy - A python toolbox for Monero
# Copyright (C) 2016 The MoneroPy Developers.
#
# MoneroPy is released under the BSD 3-Clause license. Use and redistribution of
# this software is subject to the license terms in the LICENSE file found in the
# top-level directory of this distribution.

from binascii import hexlify
import ed25519
import utils
from Keccak import Keccak

b = ed25519.b
q = ed25519.q
l = ed25519.l

_hexStrToInt = utils.hexStrToInt
_intToHexStr = utils.intToHexStr

def cn_fast_hash(s):
    return Keccak().Keccak((len(s)*4, s), 1088, 512, 0x01, 32*8, False).lower()

def sc_reduce(key):
    return _intToHexStr(_hexStrToInt(key) % l)

def public_from_int(i):
    pubkey = ed25519.encodepoint(ed25519.scalarmultbase(i))
    return hexlify(pubkey)

def public_from_secret(sk):
    return public_from_int(_hexStrToInt(sk)).decode('utf-8')

scalarmult_base = public_from_secret
