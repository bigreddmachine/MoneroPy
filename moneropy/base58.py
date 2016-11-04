# Copied in part 4 Nov 2016 from MiniNero by Shen Noether (Monero Research Lab):
#     https://github.com/shennoether/MiniNero/blob/master/MiniNero.py
#     Most recent commit: a16af1a3da601e9bce2d6e5a846754a6b4e38f98
#
# Additions and changes made to the original sources are released as specified
# in 'LICENSE' document distributed with this software.
#
# ----------
# Copyright (c) 2014-2016, The Monero Project
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of
#    conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list
#    of conditions and the following disclaimer in the documentation and/or other
#    materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be
#    used to endorse or promote products derived from this software without specific
#    prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from utils import hexStrToInt as _hexStrToInt

__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def reverseBytes(a): #input is byte string, it reverse the endianness
    b = [a[i:i+2] for i in range(0, len(a)-1, 2)]
    return ''.join(b[::-1])

def b58encode(v):
    rr = -2 * ((len(v)//2) % 16)

    a = [reverseBytes(v[i:i+16]) for i in range(0, len(v)-16, 16)]

    res = ''
    for b in a:
        bb = _hexStrToInt(b)
        result = ''
        while bb >= __b58base:
            div, mod = divmod(bb, __b58base)
            result = __b58chars[mod] + result
            bb = div
        result = __b58chars[bb] + result
        res += result
    result = ''
    if rr < 0:
        bf =  _hexStrToInt(reverseBytes(v[rr:]))
        result = ''
        while bf >= __b58base:
            div, mod = divmod(bf, __b58base)
            result = __b58chars[mod] + result
            bf = div
        result = __b58chars[bf] + result
    res += result
    return res
