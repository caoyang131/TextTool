# You can import the liborary that you need here.

import io,glob,os,struct,codecs,shutil

# function start:

def SrcImport():
    
    set_size = 0
    
    srcfolder = 'bin\\jpn\\'
    newfolder = 'bin\\chs\\'
    jpnfolder = 'txt\\jpn\\'
    chsfolder = 'txt\\chs\\'
    
    txt_encoding = 'utf_16'
    tbl1 = codecs.open('tbl\\non_chs.tbl','rb','utf_16')
    tbl2 = codecs.open('tbl\\chs.tbl','rb','utf_16')
    tbl3 = codecs.open('tbl\\test.tbl','rb','utf_16')
    
    return srcfolder,newfolder,jpnfolder,chsfolder,tbl1,tbl2,tbl3,txt_encoding,set_size
    
def Isbin(fl):
    idstring = fl.read(8)

    if idstring == b'TOMCATSD':
        binvalue = 1
    else:
        binvalue = 0
    
    return binvalue

def TxtTran(fl,fl_size,newfl,newmemory,jpnfl,chsfl,tbl_jpn,tbl_chs,tbl_test,newfilename,jpnfilename,chsfilename):

    # Write your code below:
    fl.seek(0x20)

    offset1,offset2,offset3 = struct.unpack('<3I',fl.read(0xC))
    null = fl.read(0xC)
    offset4,offset5 = struct.unpack('<2I',fl.read(0x8))
    start = fl.tell()

    size = offset1
    files = size//8

    for i in range(files):
        offset,length = struct.unpack('<2I',fl.read(0x8))
        offset += offset4
        offset += start
        breakpoint = fl.tell()
        fl.seek(offset)

        if(length > 4):
            test = fl.read(4)

            if(test == b'\x08\x0c\x1b\x7f'):
                script = fl.read(length-4).decode('cp932').replace('\n','\\n')
            else:
                fl.seek(offset)
                script = fl.read(length).decode('cp932').replace('\n','\\n')

        else:
            script = fl.read(length).decode('cp932').replace('\n','\\n')
        #print(script)
        jpnfl.write(script)
        jpnfl.write('\r\n')
        fl.seek(breakpoint)

    # Stop here.Now you can test your TranTools.Don`t modify the code below!
    return newmemory,jpnfl,chsfl
    
def test_scr(fl):
    start = fl.tell()
    #print(start)
    test2, = struct.unpack('<B',fl.read(1))
    
    while test2 != 0:
        test2, = struct.unpack('<B',fl.read(1))
        
    end = fl.tell()
    #end -= 1
    size = end
    size -= start
    fl.seek(start)
    script = fl.read(size).decode('utf8').rstrip('\x00')
    #print(script)
    #end += 1
    return script,end
