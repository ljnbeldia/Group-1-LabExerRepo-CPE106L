from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Chinook"]

# Collections
artists = db["artists"]
albums = db["Albums"]
tracks = db["tracks"]

# Fetch all artists
for artist in artists.find():
    print(f"\n Artist: {artist['Name']} (ArtistId: {artist['ArtistId']})")

    # Fetch albums for this artist
    artist_albums = albums.find({"ArtistId": artist["ArtistId"]})
    for album in artist_albums:
        print(f"   Album: {album['Title']} (AlbumId: {album['AlbumId']})")

        # Fetch tracks for this album
        album_tracks = tracks.find({"AlbumId": album["AlbumId"]})
        for track in album_tracks:
            print(f"    Track: {track['Name']} (TrackId: {track['TrackId']})")
