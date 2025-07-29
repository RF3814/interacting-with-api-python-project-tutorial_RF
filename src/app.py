import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)
#5C4PDR4LnhZTbVnKWXuDKD morat
#2piHiUbXwUNNIvYyIOIUKt francisca
id_artista="5C4PDR4LnhZTbVnKWXuDKD"
resultados=spotify.artist_top_tracks(id_artista)
print(resultados)
#canciones=[]
#for tracks in resultados['tracks']:
#    canciones.append({"nombre":tracks['name'],"popularidad":tracks['popularity'],"duracion":tracks['duration_ms']/60000})


#print(canciones)
