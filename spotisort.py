import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
import json
  
credentials = oauth2.SpotifyClientCredentials(client_id='26b486e6ddb841d190834b7dce27c20a', client_secret='f57c30c5d2e44d8385a384b85c04a687')
token = credentials.get_access_token()
token = util.prompt_for_user_token(
        username='gleekyninja22',
        scope='user-top-read',
        client_id='26b486e6ddb841d190834b7dce27c20a',
        client_secret='f57c30c5d2e44d8385a384b85c04a687',
        redirect_uri='http://google.com')
spotify = spotipy.Spotify(auth=token)

#get playlist (dict) smash bros and chill 
playlist = spotify.user_playlist('gleekyninja22', playlist_id='2GNnqVjOdPcnAUK4miJYOU', fields="tracks,next");
#get the tracks (dict)
tracks = playlist['tracks']
for i, item in enumerate(tracks['items']):
    track = item['track']
    t = track['id']
    print(str(t))
