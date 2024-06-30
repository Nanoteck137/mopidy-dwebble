import logging

from mopidy import backend, models

logger = logging.getLogger(__name__)


class DwebbleLibraryProvider(backend.LibraryProvider):
    root_directory = models.Ref.directory(uri='dwebble:',
                                          name='Dwebble')

    def browse(self, uri):
        logger.info("browse: %s", uri)
        if uri == self.root_directory.uri:
            return [
                models.Ref.directory(
                    uri = "dwebble:"+i.lower(),
                    name = i,
                ) for i in ["Artists", "Albums", "Tracks"]
            ]

        if uri.startswith("dwebble:artists"):
            res = self.backend.remote.get_all_artists()
            logger.info(str(res))
            return res

        if uri.startswith("dwebble:albums"):
            res = self.backend.remote.get_all_albums()
            return [
                self.backend.remote.album_to_ref(album) for album in res
            ]

        return []

    def get_distinct(self, field, query):
        logger.info("get_distinct ({}, {})".format(field, query))
        if field == "artist":
            return [
                artist.name for artist in self.backend.remote.get_all_artists()
            ]

        return set()

    def get_images(self, uris):
        logger.info("get_images {}".format(uris))
        return {}

    def lookup(self, uri):
        logger.info("lookup {}".format(uri))
        return []

    def refresh(self, uri):
        logger.info("refresh")
        pass

    def search(self, query, uris, exact):
        logger.info("search ({}, {}, {})".format(query, uris, exact))
        return []
