# MoneroPy - A python toolbox for Monero
# Copyright (C) 2016 The MoneroPy Developers.
#
# MoneroPy is released under the BSD 3-Clause license. Use and redistribution of
# this software is subject to the license terms in the LICENSE file found in the
# top-level directory of this distribution.

from . import mnemonic as _mn
from . import cryptonote as _cn
from . import base58 as _b58
from . import utils as _utils

ADDRESS_VERSION = "12"

def get_view_key(sk):
    '''Computes view key for input secret key.'''
    return _cn.sc_reduce(_cn.cn_fast_hash(sk))

def encode_addr(version, publicSpendKey, publicViewKey):
    '''Given address version and public spend and view keys, derive address.'''
    data = version + publicSpendKey + publicViewKey
    checksum = _cn.cn_fast_hash(data)
    return _b58.encode(data + checksum[0:8])

def decode_addr(addr):
    '''Given address, get version and public spend and view keys.'''
    d = _b58.decode(addr)
    addr_checksum = d[-8:]
    calc_checksum = _cn.cn_fast_hash(d[:-8])[:8]
    if addr_checksum == calc_checksum:
        version = d[:2]
        publicSpendKey = d[2:66]
        publicViewKey = d[66:130]
        return version, publicSpendKey, publicViewKey
    else:
        return "Invalid Address", [], []

def account_from_spend_key(sk, acct_type='simplewallet'):
    '''Given a private spend key, derive private view key and address.

    Inputs:
      - sk (str) -- private spend key
      - acct_type (str, optional) -- 'simplewallet' (default) OR 'mymonero'

    Example:
      sk, vk, addr = account_from_seed(seed)

    Outputs:
      - sk (str) -- private spend key
      - vk (str) -- private view key
      - addr (str) -- Monero address
    '''
    if acct_type == 'mymonero':
        sk_hashed = _cn.cn_fast_hash(sk)
        vk = get_view_key(sk_hashed)
        sk = _cn.sc_reduce(sk_hashed)
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
    '''Given a wallet seed, derive private spend and view keys and address.

    Inputs:
      - seed (list) -- list of seed words from which to derive account info
      - acct_type (str, optional) -- 'simplewallet' (default) OR 'mymonero'

    Example:
      sk, vk, addr = account_from_seed(seed)

    Outputs:
      - sk (str) -- private spend key
      - vk (str) -- private view key
      - addr (str) -- Monero address
    '''
    sk = _mn.mn_decode(seed)
    return account_from_spend_key(sk, acct_type)

def gen_new_wallet_seed():
    '''Generate a new, secure 25-word Monero wallet seed.

    Example:
      seed = gen_new_wallet_seed()

    Outputs:
      - seed (list) -- mnemonic recovery seed
    '''
    sk = _utils.gen_random_hex()
    seed = _mn.mn_encode(sk)
    seed.append(_mn.mn_checksum(seed))
    return seed

def gen_new_wallet():
    '''Generate a secure new wallet, including mnemonic seed, spend and view
    keys, and wallet address.

    Example:
      seed, sk, vk, addr = gen_new_wallet()

    Outputs:
      - seed (list) -- mnemonic recovery seed
      - sk (str) -- private spend key
      - vk (str) -- private view key
      - addr (str) -- Monero address
    '''
    seed = gen_new_wallet_seed()
    sk, vk, addr = account_from_seed(seed)

    return seed, sk, vk, addr

def check_address_viewkey(addr, privateViewKey):
    '''Check that a private viewkey belongs to an address.

    Example:
      isGood = check_address_viewkey(addr, privViewKey)

    Output:
      - isGood (bool)
    '''
    vs, pk, vk = decode_addr(addr)
    viewKeyValid = False
    if vk == _cn.public_from_secret(privateViewKey):
        viewKeyValid = True
    return viewKeyValid

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

        if b[33] == 2 and b[35] == 0 or b[35] == 1:
            pay_id = h[72:(72+b[34]*2-2)] # = _b58._binToHex(b[36:(36+b[34]-1)])

    elif b[0] == 2:
        if b[2] == 0 or b[2] == 1:
            pay_id = h[6:(6+b[1]*2+2)] # = _b58._binToHex(b[3:(3+b[1]+1)])

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

        if b[33] == 2 and b[35] == 0 or b[35] == 1:
            pay_id = h[72:(72+b[34]*2-2)] # = _b58._binToHex(b[36:(36+b[34]-1)])

    elif b[0] == 2:
        if b[2] == 0 or b[2] == 1:
            pay_id = h[6:(6+b[1]*2+2)] # = _b58._binToHex(b[3:(3+b[1]+1)])

        # second byte of nonce is nonce payload length
        # pubkey tag location: payload length + nonce tag byte + payload length byte
        if b[2+b[1]] == 1:
            offset = (2+b[1]) * 2 # = 2 + b[1]
            pub = h[(offset+2):(offset+2+64)] # = _b58._binToHex(b[(offset+1):(offset+1+32)])

    return pub, pay_id
