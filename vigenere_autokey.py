import sys

alphabet_b=10
alphabet_e=15*15+alphabet_b

def encrypt(key_s, message_s):
	#Change it to array to use useful methods
	key=[]
	for e in key_s:
		key.append(e)

	message=[]
	for e in message_s:
		message.append(e)
	
	cipher=[]
	i=0
	for i in range(len(message)):
		key.append(message[i])

		p = ord(message[i]) - alphabet_b
		k = ord(key[i]) - alphabet_b
		c = (p+k)%alphabet_e + alphabet_b
		cipher.append(chr(c))

	return ''.join(cipher)

def decrypt(key_s, cipher_s):
	#Change it to array to use useful methods
	key_s=key_s
	key=[]
	for e in key_s:
		key.append(e)

	cipher=[]
	for e in cipher_s:
		cipher.append(e)
	
	message=[]
	i=0
	for i in range(len(cipher)):
		c = ord(cipher[i]) - alphabet_b
		k = ord(key[i]) - alphabet_b
		p = (c-k+alphabet_e)%alphabet_e + alphabet_b
		message.append(chr(p))

		key.append(message[i])

	return ''.join(message)

##main
order=input()
if order==1:
	key=raw_input()
	with open("claro", "r") as f:
	    message=f.read()
	
	message=encrypt(key, message)

	sys.stdout.write(message)
elif order==2:
	key=raw_input()
	with open("criptografado", "rb") as f:
	    cipher=f.read()

	cipher=decrypt(key, cipher)

	sys.stdout.write(cipher)
else:
	print "Error"
