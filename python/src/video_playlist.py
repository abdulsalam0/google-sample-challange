"""A video playlist class."""
import re

class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self):
        self._playListsLib = {}

    def get_all_playlists(self):
        """ return all the avaliable playlists """
        _playlists = self._playListsLib.keys()
        _sortedList = []
        for x in self._playListsLib.keys():
            _sortedList.append(x)

        _sortedList.sort()

        if (len(_sortedList) > 0):
            print("Showing all playlists:")
            for playlist in _sortedList:
                print(playlist)
        else:
            print("No playlists exist yet")
    
    def get_all_playlist_videos(self, playlistName):
        
        if playlistName not in self._playListsLib:
            print(F"Cannot show playlist {playlistName}: Playlist does not exist")
            return
            
        _playlist_video = self._playListsLib[playlistName]
        print(F"Showing playlist: {playlistName}")
        
        if(len(_playlist_video) > 0):
            for x in _playlist_video:
                print(F"{x.title} {x.video_id} {x.tags}")
            return
                
        print("No videos here yet")

    def add_playlist_to_lib(self, playlistName):
        string_list = self._playListsLib.keys()
        string_list = [each_string.lower() for each_string in string_list]

        if playlistName.lower() in string_list:
            return "Cannot create playlist: A playlist with the same name already exists"

        self._playListsLib[playlistName] = []

        # debug
        # print(self._playListsLib)
        
        return F"Successfully created new playlist: {playlistName}"

    def add_video_to_playlist(self, playlistName, videoObj):
        
        # print(self._playListsLib, "wassup")

        name = ""

        string_titlelist = self._playListsLib.keys()
        string_titlelist = [each_string.lower() for each_string in string_titlelist]
        if playlistName.lower() in string_titlelist:
            # print("we are here")
            # string_list = self._playListsLib[playlistName]
            # string_list = [each_string.lower() for each_string in string_list]
            # _playlist = self._playListsLib[playlistName]
            # print(self._playListsLib.keys() , "playlist name")

            for value in self._playListsLib.keys():
                if re.search(playlistName, value,  re.IGNORECASE):
                    name = value;
            # print(name)
            # print(self._playListsLib.get(name))
            # print(_playlist, "nam")
            # debug
            # print(_playlist)

            if videoObj in self._playListsLib.get(name):
                # print("we entered here")
                return F"Cannot add video to {playlistName}: Video already added"
            else:
                # print("else statment")
                self._playListsLib.get(name).append(videoObj)
                return F"Added video to {playlistName}: {videoObj.title}"
        else:
            return F"Cannot add video to {playlistName}: Playlist does not exist"

    def remove_video_from_playlist(self, playlistName, video_id):

        if playlistName in self._playListsLib:
            numIndex = -1
            _playlist_video = self._playListsLib[playlistName]

            for index, video in enumerate(_playlist_video):
                if(video.video_id == video_id):
                    numIndex = index

            if(numIndex > -1):
                print(F"Removed video from {playlistName}: {self._playListsLib[playlistName][numIndex].title}")
                del self._playListsLib[playlistName][numIndex]
            else:
                print(F"Cannot remove video from {playlistName}: Video is not in playlist")
                return
            
            # debug
            # print(_playlist_video)

        else: 
            print(F"Cannot remove video from {playlistName}: Playlist does not exist")
            
    def remove_all_videos_from_playlist(self, playlistName):

        if playlistName in self._playListsLib:
            self._playListsLib[playlistName] = []
            print(F"Successfully removed all videos from {playlistName}")
        else:
            print(F"Cannot clear playlist {playlistName}: Playlist does not exist")

    def remove_playlist(self, playlistName):
        
        _playlists = self._playListsLib.keys()

        if playlistName in _playlists:
            self._playListsLib.pop(playlistName)
            print(F"Deleted playlist: {playlistName}")
        else:
            print(F"Cannot delete playlist {playlistName}: Playlist does not exist")