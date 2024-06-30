from .utils import cache
import logging
from .http import DwebbleHttpClient
from mopidy import models

logger = logging.getLogger(__name__)

class DwebbleHandler(object):
    def __init__(self, config):
        self.http = DwebbleHttpClient()

    def get_all_artists(self):
        artists = self.http.get("http://localhost:3000/api/v1/artists")["artists"]
        return artists

    def get_all_albums(self):
        albums = self.http.get("http://localhost:3000/api/v1/albums")["albums"]
        return albums

    def artist_to_ref(self, artist):
        return models.Ref.artist(
            uri = "dwebble:artist:{}".format(artist["id"]),
            name = artist["name"],
        )

    def album_to_ref(self, album):
        return models.Ref.album(
            uri = "dwebble:album:{}".format(album["id"]),
            name = album["name"],
        ) 