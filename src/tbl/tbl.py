import io,os,struct,codecs

chs = codecs.open('ChsFont.txt','rb','utf16')
jpn = codecs.open('JpnFont.txt','rb','utf16')
new = codecs.open('test.tbl','wb','utf16')

for i in jpn.read():
    tmp = i.encode('utf8')
    tmp2 = io.BytesIO()
    length = len(tmp)
    #print(length)
    for i in range(4-length):
        tmp2.write(b'\x00')

    tmp2.write(tmp)
    #print(tmp2.getvalue())
    m = ('%x' % struct.unpack('>I',tmp2.getvalue())[0])
    #print(m)
    m = m.upper()
    new.write(m)
    new.write('=')
    new.write(chs.read(1))
    new.write('\r\n')
    
new.close()
jpn.close()
chs.close()
