import streamlit as st
import joblib
import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

# Load the recommendation model
song_cluster_pipeline = joblib.load('recommendation_model.joblib')
number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
               'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']

# Set your Spotify API credentials
os.environ["SPOTIFY_CLIENT_ID"] = "16904b3cecb0467aa989231676f07a8c"
os.environ["SPOTIFY_CLIENT_SECRET"] = "191b4d3b0fad4116914e1d83c3bade53"

# Create a Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ["SPOTIFY_CLIENT_ID"],
                                                           client_secret=os.environ["SPOTIFY_CLIENT_SECRET"]))

def find_song(name, year):
    # Initialize a defaultdict to store song data
    song_data = defaultdict()

    # Search for the song using the Spotify API
    results = sp.search(q='track: {} year: {}'.format(name, year), limit=1)

    # Check if the search results contain any items
    if results['tracks']['items'] == []:
        return None

    # Extract relevant information from the search results
    results = results['tracks']['items'][0]
    track_id = results['id']
    audio_features = sp.audio_features(track_id)[0]

    # Populate the song_data dictionary with song details
    song_data['name'] = [name]
    song_data['year'] = [year]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['duration_ms'] = [results['duration_ms']]
    song_data['popularity'] = [results['popularity']]

    # Add audio features to the song_data dictionary
    for key, value in audio_features.items():
        song_data[key] = value

    # Return the song data as a DataFrame
    return pd.DataFrame(song_data)

def get_song_data(song, spotify_data):
    try:
        # Retrieve song data from the Spotify dataset based on name and year
        song_data = spotify_data[(spotify_data['name'] == song['name']) 
                                & (spotify_data['year'] == song['year'])].iloc[0]
        return song_data
    
    except IndexError:
        # If the song is not found, attempt to find it using the find_song function
        return find_song(song['name'], song['year'])

def flatten_dict_list(dict_list):
    # Flatten a list of dictionaries into a dictionary of lists
    flattened_dict = defaultdict(list)
    
    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)
            
    return flattened_dict

def get_mean_vector(song_list, spotify_data):
    # List to store vectors representing features of each song in the input list
    song_vectors = []

    for song in song_list:
        song_data = get_song_data(song, spotify_data)

        if song_data is None:
            print('Warning: {} does not exist in Spotify or in the database'.format(song['name']))
            continue

        # Ensure all vectors have the same length by filling missing values and flattening
        song_vector = song_data[number_cols].fillna(0).values.ravel()

        # Append the flattened vector to the list
        song_vectors.append(song_vector)

    if not song_vectors:
        print("Error: No valid song vectors found.")
        return None

    # Convert the list of vectors into a NumPy array and calculate the mean vector
    song_matrix = np.array(song_vectors)
    return np.mean(song_matrix, axis=0)

def recommend_songs(song_list, spotify_data, n_songs=10):
    # List of metadata columns to be included in the recommendation output
    metadata_cols = ['name', 'year', 'artists']
    # Flatten the input list of songs into a dictionary
    song_dict = flatten_dict_list(song_list)
    
    # Calculate the mean vector representing the collective features of input songs
    song_center = get_mean_vector(song_list, spotify_data)

    # Assuming 'song_cluster_pipeline' is defined elsewhere, fetch the scaler
    scaler = song_cluster_pipeline.steps[0][1]
    # Transform the entire Spotify dataset using the scaler
    scaled_data = scaler.transform(spotify_data[number_cols])
    # Transform the mean vector of input songs using the scaler
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    # Calculate cosine distances between the mean vector and all songs in the dataset
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    # Find the indices of songs with the lowest cosine distances
    index = list(np.argsort(distances)[:, :n_songs][0])
    
    # Retrieve recommended songs from the dataset based on the indices
    rec_songs = spotify_data.iloc[index]
    # Filter out songs that are already present in the input list
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]
    # Convert the recommendation DataFrame to a list of dictionaries
    return rec_songs[metadata_cols].to_dict(orient='records')

# Sample data for demonstration
data = pd.read_csv("data.csv")

# Streamlit UI
def main():
    st.title("Music Recommendation App")

    # User input for song name
    song_name = st.selectbox("Select a song:", data['name'].unique())

    # Checkbox for year selection
    song_year_option = st.checkbox("Include song year")
    if song_year_option:
        song_year = st.text_input("Enter the song year:")
        if not song_year:
            st.warning("Please enter a value for the song year.")
            st.stop()
        try:
            song_year = int(song_year)
        except ValueError:
            st.error("Please enter a valid integer for the song year.")
            st.stop()
    else:
        song_year = None

    if st.button("Recommend Songs"):
        if song_name:
            recommendations = recommend_songs([{'name': song_name, 'year': song_year}], data)

            if recommendations:
                st.header("Recommended Songs:")
                st.table(pd.DataFrame(recommendations))
            else:
                st.warning("No recommendations found for the given song.")
        else:
            st.warning("Please select a song.")

if __name__ == "__main__":
    main()
