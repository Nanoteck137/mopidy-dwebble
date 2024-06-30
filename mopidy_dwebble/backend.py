import pykka
import logging

from mopidy import backend

from mopidy_dwebble.library import DwebbleLibraryProvider
from mopidy_dwebble.remote import DwebbleHandler

logger = logging.getLogger(__name__)

class DwebbleBackend(pykka.ThreadingActor, backend.Backend):
    uri_schemes = ['dwebble']

    def __init__(self, config, audio):
        super(DwebbleBackend, self).__init__()

        self.library = DwebbleLibraryProvider(backend=self)
        # self.playback = JellyfinPlaybackProvider(audio=audio, backend=self)
        self.remote = DwebbleHandler(config)
        # self.playlists = JellyfinPlaylistsProvider(backend=self)