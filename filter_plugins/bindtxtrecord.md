bindtxtrecord
=============

This jinja filter will encapsulate BIND TXT records in quotes, when the size if shorter
than 250 characters. It will also split-up longer TXT records in multiple 250 character
blocks, quoted and surrounded by '(' and ')'.

This was mostly needed to split-up long DKIM records

mail._domainkey.ourdomain.tld descriptive text "v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhz6k3xaO8czAitz7b6k6kUhRgDpIBpA7dLpNtwZuJeav8bxMgU/w5pKGKAi5ptx3zhVdM9AWwotTeFN8jbXkygLQwFIJ22I9I7T5pM3jRHR/o4xPACP13vkbTpXGLRPG5JK1+Z/WQvd5PjKhN1OKLyN8gX2CXdOXD0De6G/qA+eRrlgBAme8r5imJsWJ" "56Qeq5+VdpY52noqEXn5bs43X0catQLjeIIzI4kuLyBBrNUuOJ/qWUJjCdZ4oO5OXbjkQ5DxBPd0GTAHY+LYcXQc7LnKP9zNjY6HAKCiOdZxaQLShkbaClhmqzltsX9IJxqFhW3BjzAA+xPptqNTNIV5PQIDAQAB"

usage
-----

{{ "%-40s IN %s %s"|format(fname, extra.type, extra.value|bindtxtrecord) }}

