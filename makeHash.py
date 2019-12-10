from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random 

rng = Random.new().read

RSAKey = RSA.generate(1024, rng)

text1 = open('alicia2.txt', 'r')
hashtext = text1.read()
text1.close

hash = MD5.new(hashtext).digest()

#signature = RSAKey.sign(hash, rng)
text2 = open('aliciaHash.txt', 'w')
text2.write(hash)
text2.close()



#print RSAKey.verify(hash, signature)
#print RSAKey.verify(hash[:-1], signature)
