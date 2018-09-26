from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, sys, time

API_KEY = ""
API_SECRET = ""
WAIT_TIME = 1
SAVE_DATA_DIR = os.path.join("image_data")

animalname = sys.argv[1]

flickr = FlickrAPI(API_KEY, API_SECRET, format="parsed-json")

result = flickr.photos.search(
    text=animalname,
    per_page=400,
    media="photos",
    sort="relevance",
    safe_search=1,
    extras="url_q, licence"
)

photos = result["photos"]
#pprint(photos)

for i, photo in enumerate(photos["photo"]):
    url_q = photo["url_q"]
    filepath = os.path.join(SAVE_DATA_DIR, animalname, photo["id"] + ".jpg")

    if os.path.exists(filepath):
        continue

    urlretrieve(url_q, filepath)

    time.sleep(WAIT_TIME)
