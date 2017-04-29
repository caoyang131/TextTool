import io,glob,os,struct,codecs,shutil

def FolderCheck(srcfolder,newfolder,jpnfolder,chsfolder):
    
    for Foldername in [srcfolder,newfolder,jpnfolder,chsfolder]:
    	if os.path.exists(Foldername) == False:
            os.makedirs(Foldername)
            
def TblSet(tbl1,tbl2,tbl3):
    tbl_jpn = {}
    tbl_chs = {}
    tbl_test = {}
    
    for lines1 in tbl1:
        line1 = lines1.split('\r\n')
        key,value = line1[0].split('=',1)
        newkey = int(str('0x' + key),16)
        tbl_chs[value] = newkey
        
    for lines2 in tbl2:
        line2 = lines2.split('\r\n')
        key,value = line2[0].split('=',1)
        newkey = int(str('0x' + key),16)
        tbl_chs[value] = newkey
        
    for lines3 in tbl3:
        line3 = lines3.split('\r\n')
        key,value = line3[0].split('=',1)
        newkey = str('0x' + key)
        newkey2 = int(str('0x' + key),16)
        tbl_jpn[int(newkey,16)] = value
        tbl_test[value] = newkey2
        
    return tbl_jpn,tbl_chs,tbl_test
    
def chs_length(chsfl,tbl_chs,newmemory):
    chs_length = len(chsfl.readline())
    chs_length *= 2
    
    for c0 in chsfl.readline():
        if c0 in tbl_chs:
            if tbl_chs[c0] < 0x100:
                chs_length -= 1
                
    newmemory.write(struct.pack('<H',chs_length))
    
def chs_script(chsfl,tbl_chs,newmemory):
    for c0 in chsfl.readline():
        if c0 in tbl_chs:
            if tbl_chs[c0] < 0x100:
                newmemory.write(struct.pack('>B',tbl_chs[c0]))
            else:
                newmemory.write(struct.pack('>H',tbl_chs[c0]))