# MoneroPy - A python toolbox for Monero.

Copyright (c) 2016 The MoneroPy Developers.  
All rights reserved.

Released under the BSD 3-Clause License. See [LICENSE](LICENSE).

## About

This Python 2/3 package aims to be a resource for Monero actions. The package
implements basic Monero cryptography, mnemonic key derivation, and key and
address creation.

## Installation

MoneroPy will be added to Python's pip once development has somewhat stabilized.

In the meantime, MoneroPy can be installed by downloading this package and then
running setup.py as follows:

    python setup.py install

## Example

Each module in MoneroPy can be imported and used separately. For example, to
create spend and view keys and derive a wallet address from a mnemonic seed,

    import moneropy.account

    seed = ["vixen", "eavesdrop", "fuming", "aching", "react", "waffle",
        "nowhere", "water", "upon", "scoop", "aztec", "sunken", "diplomat",
        "salads", "rift", "inkling", "null", "testing", "sixteen", "return",
        "kitchens", "narrate", "moisture", "nucleus", "testing"]

    spendkey, viewkey, address = moneropy.account.account_from_seed(seed)

Full documentation is under development and will be available soon.

## Unit Testing

Unit tests are available under `tests` using data from Monero software. To run
tests, navigate to the `tests` directory and execute. For example,

    python test_mnemonic.py

Tests should pass on both Python 2.x and Python 3.x. Please run tests (and write
new tests where appropriate) when submitting pull requests.

Data for testing is stored in `tests/testdata.py`.

## Disclaimer

This package uses Daniel J. Bernstein's reference Python implementation, adapted
for Python 3 compatibility. In addition, it uses Renaud Bauvin's reference
Keccak sponge function implementation (v3.2). Both are available in the public
domain, and both are written in pure Python. Therefore, key and address
derivation using MoneroPy should be considered vulnerable to side-channel
attacks, and should not be used on shared hardware to prevent, for example,
potential timing attacks.
