FILENAME_MUSH_INFO = "test.txt"
grib = "lalalё\nllfllfl\njfjjfjf`"

f = open(FILENAME_MUSH_INFO, 'wb')
f.write(grib.encode('UTF-8'))
f.close()