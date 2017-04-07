# MoneroPy - A python toolbox for Monero
# Copyright (C) 2016 The MoneroPy Developers.
#
# MoneroPy is released under the BSD 3-Clause license. Use and redistribution of
# this software is subject to the license terms in the LICENSE file found in the
# top-level directory of this distribution.

from . import account as _acc
from . import base58 as _b58
from . import cryptonote as _cn
from . import utils as _utils

KEY_SIZE = 32
HASH_SIZE = 32

def valid_hex(h):
    is_valid = True
    try:
        i = int(h, 16)
    except:
        is_valid = False
    return is_valid

def random_scalar():
    return _cn.sc_reduce32(_utils.gen_random_hex())

def hash_to_scalar(buf):
    return _cn.sc_reduce32(_cn.cn_fast_hash(buf))

def sc_mulsub(a, b, c):
    a_minus_bc = _utils.hexStrToInt(c) - _utils.hexStrToInt(a) * _utils.hexStrToInt(b)
    return _utils.intToHexStr(a_minus_bc % _cn.l)

def generate_signature(prefix_hash, pub, sec):
    err_msg = ""
    if len(sec) != KEY_SIZE*2 or valid_hex(sec) != True:
        err_msg = "Invalid secret key"
        return err_msg
    if len(prefix_hash) != HASH_SIZE*2 or valid_hex(prefix_hash) != True:
        err_msg = "Invalid prefix hash"
        return err_msg
    try:
        comm = _cn.public_from_secret(random_scalar())
        c = hash_to_scalar(prefix_hash + pub + comm)
        r = sc_mulsub(c, sec, k)
    except:
        err_msg = "There was a problem generating a signature."
        return err_msg
    return c + r

def sign_message(msg, sec, address, key_type):
    err = 0
    # Verify valid address:
    vers, psk, pvk = _acc.decode_addr(address)
    if vers == "Invalid Address":
        err = 1
        return_message = 'Address validation failed! Please check it and try again.'
        return return_message, err
    # Verify secret key:
    if key_type == "Private Spend Key":
        if _cn.public_from_secret(sec) != psk:
            err = 2
            return_message = 'Your Private Spendkey does not belong to this address!'
            return return_message, err
    else:
        if _cn.public_from_secret(sec) != pvk:
            err = 3
            return_message = 'Your Private Viewkey does not belong to this address!'
            return return_message, err
    # Sign message:
    msgHash = _cn.keccak_256(msg.encode())
    sig = generate_signature(msgHash, psk, sec)
    sig = "SigV1" + _b58.encode(sig)
    return_message = ("-----BEGIN MONERO SIGNED MESSAGE-----", msg,
        "Address: " + address, "-----BEGIN SIGNATURE-----", sig,
        "-----END MONERO SIGNED MESSAGE-----")
    return return_message, err
