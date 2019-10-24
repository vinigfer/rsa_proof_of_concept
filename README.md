RSA Proof-of-Concept
=================

How to use this:

```
python3.7
from rsa import *
rsa = RSA()
rsa.trabalho()
msg_encriptada = rsa.encrypt("Mensagem ultra-secreta", rsa.public_key)
rsa.decrypt(msg_encriptada, rsa.private_key)
```
