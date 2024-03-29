import os, sys
import PIL
from PIL import Image

size = 320, 320 

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0]+ ".thumbnail"
    if infile != outfile:
        try:
            im= Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print ("cannot create thumbnail for '%s' "% infile)
