with open("waveHeader.bin","r+b") as header:
    bytes = bytearray(header.read())
    
size = 50000

with open("test.bin", "r+b") as data:
    encrypted = bytearray(data.read())

sz=size+36
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

sz=50000
sz1=chr(sz%256)
sz=sz/256
sz2=chr(sz%256)
sz=sz/256
sz3=chr(sz%256)
sz=sz/256
sz4=chr(sz%256)

file.write(encrypted)

data.close
file.close
header.close

def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size
i=0
k=""
with open("saida.wav", 'rb') as file:
    for byte in iter(lambda: file.read(1), b''):
        i=i+1
        if i>=41:
            k=k+(byte)

file.close
file=open("arquivo.bin", "w+b")
file.write(k)