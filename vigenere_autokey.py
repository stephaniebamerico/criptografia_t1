def encrypt(key_s, message_s):
	#Change it to array to use useful methods
	key_s=key_s.upper()
	key=[]
	for e in key_s:
		key.append(e)

	message_s=message_s.upper()
	message=[]
	for e in message_s:
		message.append(e)

	#Remove spaces from message
	for unused in range(len(message)):
		if " " in message:
			message.remove(" ")
	
	cipher=[]
	i=0
	for i in range(len(message)):
		key.append(message[i])

		p = ord(message[i]) - 65
		k = ord(key[i]) - 65
		c = (p+k)%26 + 65
		cipher.append(chr(c))

	return ''.join(cipher)

def decrypt(key_s, cipher_s):
	#Change it to array to use useful methods
	key_s=key_s.upper()
	key=[]
	for e in key_s:
		key.append(e)

	cipher_s=cipher_s.upper()
	cipher=[]
	for e in cipher_s:
		cipher.append(e)
	
	message=[]
	i=0
	for i in range(len(cipher)):
		c = ord(cipher[i]) - 65
		k = ord(key[i]) - 65
		p = (c-k+26)%26 + 65
		message.append(chr(p))

		key.append(message[i])

	return ''.join(message)

###

k=raw_input("Chave: ")
m=raw_input("Msg: ")

print decrypt(k, m)