def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

with open("waveHeader.bin","r+b") as header:
    bytes = bytearray(header.read())

data = open("test.bin", "rb")    
size = getSize(data)
with open("test.bin", "r+b") as data:
    encrypted = bytearray(data.read())

with open("random.bin", "r+b") as randomFile:
    random = bytearray(randomFile.read())

sz=size+36+100000 #size eh o tam. do arquivo criptografado, 
                  #100000 eh o tam um arquivo random pra deixar o audio mais comprido
#tentei fazer um "for" e deu ruim, fica faltando pedaco
sz1=chr(sz%256)
sz=sz/256
sz2=chr(sz%256)
sz=sz/256
sz3=chr(sz%256)
sz=sz/256
sz4=chr(sz%256)

file=open("saida.wav", "w+b")

file.write("RIFF")
file.write(sz1)
file.write(sz2)
file.write(sz3)
file.write(sz4)
file.write("WAVE")
file.write(bytes)
file.write("data")

file.write(random)
file.write(encrypted)

data.close
randomFile.close
file.close
header.close


#essa e a parte que le o arquivo
i=0
k=""
with open("saida.wav", 'rb') as file:
    for byte in iter(lambda: file.read(1), b''):
        i=i+1
        if i>=41+100000:
            k=k+(byte)

file.close
file=open("arquivo.bin", "w+b")
file.write(k)
