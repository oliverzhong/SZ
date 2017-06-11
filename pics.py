# encoding=utf-8
import os
import shutil

# path = 'D:\pic'
def pics_(path):
    upath = unicode(path, 'utf-8')
    dirs = os.listdir(upath)
    for item in ['jpg', 'bmp', 'tif', 'gif', 'png']:
        path_new = os.path.join(upath, item)
        if os.path.exists(path_new) == False:
            os.makedirs(path_new)
    for dr in dirs:
        idx = dr.split('.')
        if idx[-1] == 'jpg':
          shutil.move(os.path.join(upath, dr), os.path.join(upath, 'jpg'))
        elif idx[-1] == 'bmp':
          shutil.move(os.path.join(upath, dr), os.path.join(upath, 'bmp'))
        elif idx[-1] == 'tif':
          shutil.move(os.path.join(upath, dr), os.path.join(upath, 'tif'))
        elif idx[-1] == 'png':
          shutil.move(os.path.join(upath, dr), os.path.join(upath, 'png'))
        elif idx[-1] == 'gif':
          shutil.move(os.path.join(upath, dr), os.path.join(upath, 'gif'))
        else:
          shutil.move(os.path.join(upath, dr), os.path.join(upath, 'other'))
    return 'ok'