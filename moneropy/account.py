# MoneroPy - A python toolbox for Monero
# Copyright (C) 2016 The MoneroPy Developers.
#
# MoneroPy is released under the BSD 3-Clause license. Use and redistribution of
# this software is subject to the license terms in the LICENSE file found in the
# top-level directory of this distribution.

import mnemonic as _mn
import cryptonote as _cn
import base58 as _b58

ADDRESS_VERSION = "12"

def get_view_key(sk):
    '''Computes view key for input secret key.'''
    return _cn.sc_reduce(_cn.cn_fast_hash(sk))

def encode_addr(version, publicSpendKey, publicViewKey):
    data = version + publicSpendKey + publicViewKey
    checksum = _cn.cn_fast_hash(data)
    return _b58.b58encode(data + checksum[0:8])

def account_from_secret_key(sk, acct_type='simplewallet'):
    if acct_type == 'mymonero':
        vk = get_view_key(sk)
        sk = _cn.sc_reduce(sk)
    elif acct_type == 'simplewallet':
        sk = _cn.sc_reduce(sk)
        vk = get_view_key(sk)
    else:
        raise Exception("Account type not valid.")

    pk = _cn.public_from_secret(sk)
    pvk = _cn.public_from_secret(vk)

    addr = encode_addr(ADDRESS_VERSION, pk, pvk)

    return sk, vk, addr

def account_from_seed(seed, acct_type='simplewallet'):
    sk = _mn.mn_decode(seed)
    return account_from_secret_key(sk, acct_type)
