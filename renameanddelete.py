import os
from os import remove

os.rename('myoutputimage.jpg', 'myoutputimage2.jpg')

remove('myoutputimage2.jpg')
