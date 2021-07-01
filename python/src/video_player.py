"""A video player class."""
import random
import re

from .video_library import VideoLibrary

from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    # creating state
    videoPlaying = False
    currentVideo = None
    pausedVideo = False


    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playlist_obj = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        titlesList = []

        print("Here's a list of all available videos:")
        for video in self._video_library.get_all_videos():
            _tags = str(list(video.tags)).replace(",","").replace("'","")
            titlesList.append(F"{video.title} ({video.video_id}) {_tags}")
        titlesList.sort()

        for x in titlesList:
            print(x)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        #  check if video exist
        if(self._video_library.get_video(video_id) == None):
            print("Cannot play video: Video does not exist")

        #  stopping and starting a new video use case 
        elif(self.videoPlaying and self.currentVideo != None):
            print(F"Stopping video: {self.currentVideo.title}")
            self.currentVideo = self._video_library.get_video(video_id)
            self.pausedVideo = False
            print(F"Playing video: {self._video_library.get_video(video_id).title}")

        # playing a video use case
        elif(self.videoPlaying == False and self.currentVideo == None):
            self.videoPlaying = True
            self.currentVideo = self._video_library.get_video(video_id)        
            print(F"Playing video: {self._video_library.get_video(video_id).title}")
        
    def stop_video(self):
        """Stops the current video."""

        if(self.videoPlaying == False):
            print("Cannot stop video: No video is currently playing") 
        else:
            self.videoPlaying = False
            print(F"Stopping video: {self.currentVideo.title}")
            self.currentVideo = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        # print("length of the array",len(self._video_library.get_all_videos()))
        # print(random.randint(0,len(self._video_library.get_all_videos())-1))

        selectedNum = random.randint(0,len(self._video_library.get_all_videos())-1)
        if(self.videoPlaying and self.currentVideo != None):
            print(F"Stopping video: {self.currentVideo.title}")
            self.currentVideo = self._video_library.get_all_videos()[selectedNum]
            print(F"Playing video: {self._video_library.get_all_videos()[selectedNum].title}")
        else:
            self.videoPlaying = True
            self.currentVideo = self._video_library.get_all_videos()[selectedNum]       
            print(F"Playing video: {self._video_library.get_all_videos()[selectedNum].title}")

    def pause_video(self):
        """Pauses the current video."""
        # check if video is running
        if(self.currentVideo == None):
            print("Cannot pause video: No video is currently playing")

        # video already paused
        elif(self.pausedVideo):
            print(F"Video already paused: {self.currentVideo.title}")

        # pause the video
        elif(self.videoPlaying and self.currentVideo != None):
            print(F"Pausing video: {self.currentVideo.title}")
            self.pausedVideo = True

    def continue_video(self):
        """Resumes playing the current video."""

        if(self.currentVideo == None):
            print("Cannot continue video: No video is currently playing")

        elif(self.pausedVideo == False):
            print("Cannot continue video: Video is not paused")
        
        elif(self.pausedVideo):
            self.pausedVideo = False
            self.videoPlaying = True
            print(F"Continuing video: {self.currentVideo.title}")

    def show_playing(self):
        """Displays video currently playing."""

        

        if(self.currentVideo == None):
            print("No video is currently playing")
            return

        _title = self.currentVideo.title
        _id = self.currentVideo.video_id
        _tags = str(list(self.currentVideo.tags)).replace(",","").replace("'","")

        if(self.pausedVideo == True):
            print(F"Currently playing: {_title} ({_id}) {_tags} - PAUSED")
        
        else:
            print(F"Currently playing: {_title} ({_id}) {_tags}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        print(self._video_playlist_obj.add_playlist_to_lib(playlist_name))

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        name = ""

        for value in (self._video_playlist_obj._playListsLib.keys()):
            if re.search(playlist_name, value,  re.IGNORECASE):
                    name = value;
        
        if(name == ""):
            print(F"Cannot add video to {playlist_name}: Playlist does not exist")
            return

        if(self._video_library.get_video(video_id) != None):
            print(self._video_playlist_obj.add_video_to_playlist(playlist_name, self._video_library.get_video(video_id)))
        else:
            print(F"Cannot add video to {playlist_name}: Video does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        self._video_playlist_obj.get_all_playlists();
        # print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        self._video_playlist_obj.get_all_playlist_videos(playlist_name)
        # print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        name = ""

        for value in (self._video_playlist_obj._playListsLib.keys()):
            if re.search(playlist_name, value,  re.IGNORECASE):
                    name = value;
        
        if(name == ""):
            print(F"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        
        if(self._video_library.get_video(video_id) != None):
            self._video_playlist_obj.remove_video_from_playlist(playlist_name,video_id)
        else:
            print(F"Cannot remove video from {playlist_name}: Video does not exist")

        # print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        self._video_playlist_obj.remove_all_videos_from_playlist(playlist_name)
        
        # print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        self._video_playlist_obj.remove_playlist(playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        index = 1
        answersList = []
        for video in self._video_library.get_all_videos():
            # print(F"{video.title} {video.video_id} {video.tags}")
            if re.search(F"{search_term}", video.title, re.IGNORECASE):
                answersList.append(video)
                print(F"{index}) {video.title} ({video.video_id}) {video.tags}")
                index += 1
        print("Would you like to play any of the above? If yes, specify the number of the video.If your answer is not a valid number, we will assume it's a no.")

        # print(answersList[1])
        StrNum = input("")
        num = int(StrNum)
        if(num < (len(answersList)+ 1) and num > 0):
            print(F"Playing video: {answersList[num-1].title}")
        else:
            print(F"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        index = 1
        answersList = []
        for video in self._video_library.get_all_videos():
            # print(video.tags)
            for tag in video.tags:
                if re.search(F"{video_tag}", tag, re.IGNORECASE):
                    answersList.append(video)
                    print(F"{index}) {video.title} ({video.video_id}) {video.tags}")
                    index += 1
            # if re.search(F"{search_term}", video.title, re.IGNORECASE):
        print("Would you like to play any of the above? If yes, specify the number of the video.If your answer is not a valid number, we will assume it's a no.")

        StrNum = input("")
        num = int(StrNum)
        if(num < (len(answersList)+ 1) and num > 0):
            print(F"Playing video: {answersList[num-1].title}")
        else:
            print(F"No search results for {video_tag}")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
