_trash="X"

##Input: encryption key
##Output: matrix built
def build_matrix(key):
	#Create the matrix/vector from the key
	v_matrix=[]
	for e in key.upper():
		if e not in v_matrix:
			v_matrix.append(e)

	#Complete the matrix with alphabet
	alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"

	for e in alphabet:
		if e not in v_matrix:
			v_matrix.append(e)

	#"Initializes" the matrix 5x5
	matrix=[]
	for e in range(5):
		matrix.append('')

	#Break it into 5*5
	matrix[0]=v_matrix[0:5]
	matrix[1]=v_matrix[5:10]
	matrix[2]=v_matrix[10:15]
	matrix[3]=v_matrix[15:20]
	matrix[4]=v_matrix[20:25]
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
	message_original=message_original.upper()
	#Change it to array to use useful methods
	message=[]
	for e in message_original:
		message.append(e)

	#Remove spaces from message
	for unused in range(len(message)):
		if " " in message:
			message.remove(" ")

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
	for i in range(5):
		for j in range(5):
			if key_matrix[i][j]==letter:
				x=i
				y=j

	return x,y

def encrypt(message):
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
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			cipher.append(key_matrix[p1][q1+1])
			cipher.append(key_matrix[p1][q2+1])
		#If letters in the same column, circular shift below
		elif q1==q2:
			if p1==4:
				p1=-1;
			if p2==4:
				p2=-1;
			cipher.append(key_matrix[p1+1][q1])
			cipher.append(key_matrix[p2+1][q2])
		else:
			cipher.append(key_matrix[p1][q2])
			cipher.append(key_matrix[p2][q1])
	return ''.join(cipher)

##
def decrypt(cipher):
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
			if q1==4:
				q1=-1
			if q2==4:
				q2=-1
			plaintext.append(key_matrix[p1][q1-1])
			plaintext.append(key_matrix[p1][q2-1])		
		#If letters in the same column, circular shift above
		elif q1==q2:
			if p1==4:
				p1=-1;
			if p2==4:
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
print "Playfair Cipher"
order=input("Choose :\n1,Encrypting \n2,Decrypting\n")
if order==1:
	key=raw_input("Please input the key : ")
	message=raw_input("Please input the message : ")
	print "Encrypting: \n"+"Message: "+message
	print "Cipher: " 
	print encrypt(message)
elif order==2:
	key=raw_input("Please input the key : ")
	cipher=raw_input("Please input the cipher text: ")
	#cipher="ILSYQFBWBMLIAFFQ"
	print "\nDecrypting: \n"+"Cipher: "+cipher
	print "Plaintext:"
	print decrypt(cipher)
else:
	print "Error"