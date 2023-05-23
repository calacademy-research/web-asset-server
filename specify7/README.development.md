Setting up for development:
Set up image web-image-sever per readme.development.md in that repo.

in docker-compose.yml change all ASSET_SERVER_URLs to your local asset server url (let it run on port 80):
e.g.:

- ASSET_SERVER_URL=http://192.168.1.223/web_asset_store.xml

using your absolute IP (not 127.0.0.1 or localhost).  [may not need this but it's working and I'm tired of fooling around with it]

under nginx, change port from 80 to something else:

    image: nginx
    ports:
      - "9090:80"




