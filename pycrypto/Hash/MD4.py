##https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Hash/MD4.py

from Crypto.Hash import MD4
h = MD4.new()
h.update(b'Hello')
print h.hexdigest()

