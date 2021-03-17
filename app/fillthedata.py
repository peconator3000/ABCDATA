from app import models
from app.models import SModel
from app import db
import glob
import os
def fill_db(objfiles): 
    objfiles=glob.glob(objfiles)
           
    for file in objfiles:
        
         imname=os.path.relpath(file)
         index=imname.index('.')
         imname=imname[4:index]
         print(imname)
         
         nname=os.path.basename(file)
         index=nname.index('.')
         nname=nname[:index]
         obj = SModel(name=str(nname),path=str(imname))
         db.session.add(obj)
         db.session.commit()
         obj.ReturnPath()
