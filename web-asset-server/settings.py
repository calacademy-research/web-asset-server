import os

# Sample Specify web asset server settings.

# Turns on bottle.py debugging, module reloading and printing some
# information to console.
DEBUG = True

# This secret key is used to generate authentication tokens for requests.
# The same key must be set in the Web Store Attachment Preferences in Specify.
# A good source for key value is: https://www.grc.com/passwords.htm
# Set KEY to None to disable security. This is NOT recommended since doing so
# will allow anyone on the internet to use the attachment server to store
# arbitrary files.
KEY = 'xXeLi2YsYgNwD2io'

# Auth token timestamp must be within this many seconds of server time
# in order to be considered valid. This prevents replay attacks.
# Set to None to disable time validation.
TIME_TOLERANCE = 150

# Set this to True to require authentication for downloads in addition
# to uploads and deletes.  Static file access, if enabled, is not
# affected by this setting.
REQUIRE_KEY_FOR_GET = False

# This is required for use with the Web Portal.
# Enables the 'getfileref' and '/static/...' URLs.
ALLOW_STATIC_FILE_ACCESS = True

# These values are interpolated into the web_asset_store.xml resource
# so the client knows how to talk to the server.
# HOST = '192.168.1.224'

# Image server host and port info
if "EXTERNAL_IP" in os.environ:
    HOST = os.getenv('EXTERNAL_IP')
    # print(f"Got external Ip from environment:{HOST}")
else:
    import socket


    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    HOST = local_ip
    # print(f"Got external Ip from gethostbyname:{HOST}")


PORT = 80
# HOST='127.0.0.1'
import socket

# Get the hostname of the local machine
hostname = socket.gethostname()

# Get the IP address of the local machine
HOST = f'{socket.gethostbyname(hostname)}'

# print("Hostname:", hostname)
# print("IP Address:", ip_address)

#HOST='10.2.200.83'
#HOST='10.1.12.109'
# HOST='ibss-images.calacademy.org'
SERVER_NAME = HOST
SERVER_PORT = PORT

# Port the development test server should listen on.
DEVELOPMENT_PORT = PORT



# Base directory for all attachments.
BASE_DIR = './attachments/'

# Originals and thumbnails are stored in separate directories.
THUMB_DIR = 'thumbnails'
ORIG_DIR = 'originals'

# Set of mime types that the server will try to thumbnail.
CAN_THUMBNAIL = {'image/jpeg', 'image/gif', 'image/png', 'image/tiff', 'application/pdf'}

# What HTTP server to use for stand-alone operation.
# SERVER = 'paste' # Requires python-paste package. Fast, and seems to work good.
SERVER = 'wsgiref'  # For testing. Requires no extra packages.

#Image databse connection information
SQL_USER='root'
SQL_PASSWORD='password'
SQL_HOST='127.0.0.1'
SQL_PORT=3308
SQL_DATABASE='images'
