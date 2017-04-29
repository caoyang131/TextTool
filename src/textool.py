import io,glob,os,struct,codecs,shutil
from textran import *
from libtext import *

srcfolder,newfolder,jpnfolder,chsfolder,tbl1,tbl2,tbl3,txt_encoding,set_size = SrcImport()

FolderCheck(srcfolder,newfolder,jpnfolder,chsfolder)

files = glob.iglob(srcfolder+'*.bin')
   
tbl_jpn,tbl_chs,tbl_test = TblSet(tbl1,tbl2,tbl3)

#=============================================

print('============================================')
print('        Project ScrTool Version 1.00        ')
print('')
print('           Written by caoyang131            ')
print('============================================')
print('')
print('                Let`s start!                ')
print('')
print('============================================')
print('')

#=============================================
txtcheckid = 1

for srcbin in files:
    fl = open(srcbin,'rb')
    fl_size = os.path.getsize(srcbin)
    binname = os.path.basename(srcbin)
    binbasename,extname = os.path.splitext(binname)
    newfilename = str(newfolder + binbasename + extname)
    jpnfilename = str(jpnfolder + binbasename + '.txt')
    chsfilename = str(chsfolder + binbasename + '.txt')
    
    binvalue = Isbin(fl)
    
    if fl_size > set_size and binvalue == 1:
        
        newmemory = io.BytesIO()
        newfl = open(newfilename,'wb')
        jpnfl = codecs.open(jpnfilename,'wb',txt_encoding)
        
        if os.path.isfile(chsfilename) == False:
            chsfl = jpnfl
            print(srcbin + ' >> ' + jpnfilename)
        
        else:
            chsfl = codecs.open(chsfilename,'rb',txt_encoding)
            print(chsfilename + ' >> ' + newfilename)
        
        newmemory,jpnfl,chsfl = TxtTran(fl,fl_size,newfl,newmemory,jpnfl,chsfl,tbl_jpn,tbl_chs,tbl_test,newfilename,jpnfilename,chsfilename)
        
        newfl.write(newmemory.getvalue())
        newfl.close()
        jpnfl.close()
        chsfl.close()
        fl.close()
    
    else:
        shutil.copyfile(srcbin,newfilename)
