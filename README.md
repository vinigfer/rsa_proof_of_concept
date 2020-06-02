RSA Proof-of-Concept
=================

How to use this:

```
python3.7
from rsa import 
rsa = RSA()
rsa.setup()
mensagem_encriptada = rsa.encrypt("Mensagem ultra-secreta", rsa.public_key)
rsa.decrypt(mensagem_encriptada, rsa.private_key)
```

Or you can run individual steps one by one, and see the created values:
```
python3.7
from rsa import *
rsa = RSA()

p = find_prime_with_fermat()
q = find_prime_with_fermat()

rsa.set_p(p)
rsa.set_q(q)
rsa.calculate_n()
rsa.calculate_phi()
rsa.generate_e()
rsa.calculate_d()

mensagem_encriptada = rsa.encrypt("Mensagem ultra-secreta", rsa.public_key)
rsa.decrypt(mensagem_encriptada, rsa.private_key)
```
