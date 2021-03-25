from app.models import SModel
from app import db
import glob
import os
# python obj2png.py -i bunny.obj -a -95 -e 100


def fill_db(objfiles):
    # TODO cюде генерацию png из obj

    objfiles = glob.glob(objfiles)

    for file in objfiles:
        imname = os.path.relpath(file)
        index = imname.index('.')
        imname = imname[4:index]
        print(imname)

        nname = os.path.basename(file)
        index = nname.index('.')
        nname = nname[:index]
        obj = SModel(name=str(nname), path=str(imname))
        db.session.add(obj)
        db.session.commit()
        obj.ReturnPath()
