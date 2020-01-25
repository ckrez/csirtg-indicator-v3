import pytricia

_V4_RESERVED = {
    '0.0.0.0/8',
    '10.0.0.0/8',
    '100.64.0.0/10',
    '127.0.0.0/8',
    '169.254.0.0/16',
    '172.16.0.0/12',
    '192.0.0.0/24',
    '192.0.0.0/29',
    '192.0.0.8/32',
    '192.0.0.9/32',
    '192.0.0.10/32',
    '192.0.0.170/32',
    '192.0.0.171/32',
    '192.0.2.0/24',
    '192.31.196.0/24',
    '192.52.193.0/24',
    '192.88.99.0/24',
    '192.168.0.0/16',
    '192.175.48.0/24',
    '198.18.0.0/15',
    '198.51.100.0/24',
    '203.0.113.0/24',
    '240.0.0.0/4',
    '255.255.255.255/32',
}

# http://www.iana.org/assignments/ipv6-multicast-addresses/ipv6-multicast-addresses.xhtml
_V6_RESERVED = {
    '::1/128',
    '::/128',
    '::ffff:0:0/96',
    '64:ff9b::/96',
    '64:ff9b:1::/48',
    '100::/64',
    '2001::/23',
    '2001::/32',
    '2001:1::1/128',
    '2001:1::2/128',
    '2001:2::/48',
    '2001:3::/32',
    '2001:4:112::/48',
    '2001:5::/32',
    '2001:10::/28',
    '2001:20::/28',
    '2001:db8::/32',
    '2002::/16',
    '2620:4f:8000::/48',
    'fc00::/7',
    'fe80::/10',
}

V4_RESERVED = pytricia.PyTricia()
V6_RESERVED = pytricia.PyTricia()

for k in _V4_RESERVED:
    V4_RESERVED.insert(k, True)

for k in _V6_RESERVED:
    V6_RESERVED[k] = True