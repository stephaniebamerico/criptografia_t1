import sys

_trash=chr(228)
alphabet_b=10
alphabet_e=15*15+alphabet_b

##Input: encryption key
##Output: matrix built
def build_matrix(key):
	#Create the matrix/vector from the key
	v_matrix=[]
	for e in key:
		if e not in v_matrix:
			v_matrix.append(e)

	#Complete the matrix with alphabet
	for a in range(alphabet_b,alphabet_e):
		e=chr(a)
		if e not in v_matrix:
			v_matrix.append(e)

	#"Initializes" the matrix 15x15
	matrix=[]
	for e in range(15):
		matrix.append('')

	#Break it into 5*5
	for e in range(15):
		matrix[e]=v_matrix[e*15:(e+1)*15]

	return matrix

##Input: array with message
##Output: array of digraphs
def array_to_digraphs(message):
	i=0
	digraphs=[]
	for x in range(len(message)/2):
		digraphs.append(message[i:i+2])
		i=i+2
	return digraphs

##Input: original message
##Output: vector of digraphs
def clear_message(message_original):
	#Change it to array to use useful methods
	message=[]
	for e in message_original:
		message.append(e)

	#If both letters are the same, add an "X" after the first letter.
	i=0
	for e in range(len(message)/2):
		if message[i]==message[i+1]:
			message.insert(i+1,_trash)
		i=i+2

	#If it is odd digit, add an "X" at the end
	if len(message)%2==1:
		message.append(_trash)
	
	return message

##Input: matrix for cipher, letter
##Output: encrypted letter
def find_position(key_matrix,letter):
	x=y=0
	for i in range(15):
		for j in range(15):
			if key_matrix[i][j]==letter:
				x=i
				y=j

	return x,y

def encrypt_pf(key, message):
	#Clear/format message
	message=clear_message(message)
	#Create list of diagraphs from the message
	message=array_to_digraphs(message)
	#Create matrix from key
	key_matrix=build_matrix(key)
	
	#For each digraph, encrypted according to the matrix
	cipher=[]
	for e in message:
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])

		#If letters on the same line, circular shift on the right
		if p1==p2:
			if q1==14:
				q1=-1
			if q2==14:
				q2=-1
			cipher.append(key_matrix[p1][q1+1])
			cipher.append(key_matrix[p1][q2+1])
		#If letters in the same column, circular shift below
		elif q1==q2:
			if p1==14:
				p1=-1;
			if p2==14:
				p2=-1;
			cipher.append(key_matrix[p1+1][q1])
			cipher.append(key_matrix[p2+1][q2])
		else:
			cipher.append(key_matrix[p1][q2])
			cipher.append(key_matrix[p2][q1])
	return ''.join(cipher)

##
def decrypt_pf(key, cipher):
	#Create list of diagraphs from the cipher
	cipher=array_to_digraphs(cipher)
	#Create matrix from key
	key_matrix=build_matrix(key)

	#For each digraph, decrypted according to the matrix
	plaintext=[]
	for e in cipher:
		p1,q1=find_position(key_matrix,e[0])
		p2,q2=find_position(key_matrix,e[1])
		#If letters on the same line, circular shift on the left
		if p1==p2:
			if q1==14:
				q1=-1
			if q2==14:
				q2=-1
			plaintext.append(key_matrix[p1][q1-1])
			plaintext.append(key_matrix[p1][q2-1])		
		#If letters in the same column, circular shift above
		elif q1==q2:
			if p1==14:
				p1=-1;
			if p2==14:
				p2=-1;
			plaintext.append(key_matrix[p1-1][q1])
			plaintext.append(key_matrix[p2-1][q2])
		else:
			plaintext.append(key_matrix[p1][q2])
			plaintext.append(key_matrix[p2][q1])

	#Remove "X" inserted in the encryption
	for unused in range(len(plaintext)):
		if _trash in plaintext:
			plaintext.remove(_trash)
	
	#Convert array to string
	return ''.join(plaintext)

##main
order=input()
if order==1:
	key=raw_input()
	with open("claro", "r") as f:
	    message=f.read()
	
	message=encrypt_pf(key, message)

	sys.stdout.write(message)
elif order==2:
	key=raw_input()
	with open("criptografado", "rb") as f:
	    cipher=f.read()

	cipher=decrypt_pf(key, cipher)

	sys.stdout.write(cipher)
else:
	print "Error"