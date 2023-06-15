There are three major parts to the "specify sandbox". the first is the
specify database itself, which runs on mysql. Get a copy of a backup of the
database and install it per the insrcutions in "database". you'll be using
a docker based DB instance, and likely only hosting a single collection's worth
of data, though hosting/restoring all is quite possible.

Next, get the image server working. This is relatively simple - it's 
in web-asset-server. you will be creating this with no data, so creating a second
mysql database (this one on port 3308 instead of the default 3306) will be sufficent.
Check out the entire web asset server per the link in the readme and use the settings
and utilities in web-asset-server to overwrite its defaults.

Finally, run docker-compose start in the specify7 directory after updating the
ip address per the instructions.

for specify7, pull: git@github.com:specify/specify7.git
git clone git@github.com:specify/specify7.git in this directory and then copy
the contents of specify-7-config over the files in this dir

for web asset server, pull: https://github.com/calacademy-research/web-asset-server
git clone https://github.com/calacademy-research/web-asset-server
then copy the contents of web-asset-server-config over the files in this new dir
