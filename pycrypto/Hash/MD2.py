##https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Hash/MD2.py

from Crypto.Hash import MD2

h = MD2.new()
h.update(b'Hello')
print h.hexdigest()