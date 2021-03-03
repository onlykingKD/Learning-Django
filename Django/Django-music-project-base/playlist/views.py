from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.

# NOTE: THESE PLAYLISTS AND SONG LISTS ARE NOT TO BE MODIFIED
my_playlists=[
    {"id":1,"name":"Bicycle Playlist","numberOfSongs":3},
    {"id":2,"name":"Coding Playlist","numberOfSongs":2}
]


my_songs = [
    {"id": 1, "Track": "thank u, next", "Artist": "Ariana Grande", "Album": "thank u, next", "Length": "3:27","playlist_id": 1},
    {"id": 2, "Track": "Better Now", "Artist": "Post Malone", "Album": "beerbongs & bentleys", "Length": "3:51","playlist_id": 1},
    {"id": 3, "Track": "The Middle", "Artist": "Grey,Marren Morris, ZEDD", "Album": "The Middle", "Length": "3:04","playlist_id": 1},
    {"id": 4, "Track": "Love Lies", "Artist": "Normani, Khalid", "Album": "Love Lies", "Length": "3:21","playlist_id": 2},
    {"id": 5, "Track": "Rise", "Artist": "Jack & Jack, Jonas Blue", "Album": "Blue", "Length": "3:14","playlist_id": 2},
]

# NOTE: The home view is already implemented for you, you just need to map it to the URL :)
def home(request):
    return render(request,'playlist/home.html',{"my_playlists":my_playlists})

def about(request):     
    return HttpResponse("""<h1>About Us:</h1><p>With us, you can easily find the music of your choice and easily share it with other people. You can also browse through the collections of friends, artists, and celebrities, or create a playlist of your own. Soundtrack your life with us. Subscribe or listen for free.</p>""")

def playlist(request,id):
    songs = []
    for i in my_songs:
        if(i["playlist_id"] == id):
            songs.append(i)
            playlist_name = my_playlists[id-1]["name"]
    
    if(len(songs) == 0):
        raise Http404

    return render(request, 'playlist/songs.html', {"songs" : songs, "playlist_name" : playlist_name})
#     #  Complete this method and map it to the URL that takes id, i.e. localhost:8000/playlist/<id>

#     # The logic to find the songs for this playlist

#     # Find the playlist name

#     # Make sure you return 404 in case playlist id is not present

#     # HINT: return will look something like the below:
#     # return render(request,'??template_file_name??', {"songs": ?? "playlist_name": ?? })