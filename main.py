import sys
from rail_fence import encrypt_rf
from rail_fence import decrypt_rf
from playfair import encrypt_pf
from playfair import decrypt_pf
from gera_audio import geraSaida

key_rf=raw_input()
m=raw_input()
aux=encrypt_rf(list(key_rf),list(m))
encrypted_rf=''.join(aux)

print "Texto Claro:"
sys.stdout.write(m)
print
print

key_pf=raw_input()
print "Criptografado Rail Fence:"
sys.stdout.write(encrypted_rf)
print
print

encrypted_pf=encrypt_pf(key_pf, encrypted_rf)

print "Criptografado playfair:"
sys.stdout.write(encrypted_pf)
print
print

geraSaida(encrypted_pf)

cipher=decrypt_pf(key_pf,encrypted_pf)
print "Decriptado playfair:"
sys.stdout.write(cipher)
print
print

saida=decrypt_rf(list(key_rf),list(cipher))
output=''.join(saida)
print "Decriptado Rail Fence:"
print output




#    key=raw_input()
#    with open("criptografado", "rb") as f:
#        cipher=f.read()

#    cipher=decrypt(key, cipher)

#    sys.stdout.write(cipher)
