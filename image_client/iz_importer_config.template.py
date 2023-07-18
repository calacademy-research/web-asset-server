SPECIFY_DATABASE_HOST = '127.0.0.1'
SPECIFY_DATABASE_PORT = 3306
SPECIFY_DATABASE = 'casiz'
USER = 'redacted'
PASSWORD = 'redacted'

COLLECTION_NAME = 'IZ'

MINIMUM_ID_DIGITS = 5
MAXIMUM_ID_DIGITS = 12

IMAGE_EXTENSION='(.(jpg|jpeg|tiff|tif|png))$'
IMAGE_SUFFIX = f'[a-z\-\(\)0-9 ©_,.]*{IMAGE_EXTENSION}'
CASIZ_NUMBER = '([0-9]{' + str(MINIMUM_ID_DIGITS) + ','+ str(MAXIMUM_ID_DIGITS)+'})'
CASIZ_PREFIX = 'cas(iz)?[#a-z _]*[_ \-]?'
CASIZ_MATCH = CASIZ_PREFIX + CASIZ_NUMBER
FILENAME_MATCH = CASIZ_MATCH


FILENAME_CONJUNCTION_MATCH = '(' + CASIZ_MATCH + f'(([ ]*(and|or)[ ]*({CASIZ_PREFIX})?{CASIZ_NUMBER}))' + '{1,})'

# Two sources, with some redundancy.
# //hydra/data/izg/IZ Images maps to /Volumes/data/izg/IZ\ Images
# //pegasus/images/izg/IZ maps to /Volumes/images/izg/iz

# CRRF & decoder ring #1:
# /Volumes/data/izg/IZ Images/CRRF Colln Specimen Photos_CRRF acknowledgements required

IZ_SCAN_FOLDERS = [
    f'/volumes/data/izg/iz images',  # core images - hydra
    f'/Volumes/images/izg/iz',  # core images - pegasus
    f'/Volumes/data/izg/IZ Images/CASIZ Label Images' # label data
]
# https://exiv2.org/tags.html
EXIF_DECODER_RING = {
    315: 'Artist',
    33432: 'Copyright',
    270: 'ImageDescription'
}

