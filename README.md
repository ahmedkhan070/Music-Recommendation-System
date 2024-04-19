# Music Recommendation System

This project demonstrates how to build a music recommendation system using a Spotify dataset. The system employs K-means clustering to recommend similar music tracks based on the features of tracks. Additionally, it includes a Streamlit app that provides a user-friendly interface for inputting a track and receiving recommendations for similar tracks.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Data](#data)
- [Recommendation Algorithm](#recommendation-algorithm)
- [Code Explanation](#code-explanation)
- [References](#references)

## Introduction

The music recommendation system suggests similar music tracks based on the features of tracks from a Spotify dataset. The system uses K-means clustering to group tracks into clusters based on their audio features and recommend similar tracks from the same cluster.

The project includes a Streamlit app that provides a user-friendly interface for inputting a music track and receiving recommendations for similar tracks.

## Features

- Uses a Spotify dataset for music recommendations.
- Implements K-means clustering to group tracks based on their audio features.
- Streamlit app for recommending music based on user input.

## Setup and Installation

1. **Clone the Repository**:
    - Clone the project repository to your local machine.
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a Virtual Environment**:
    - Create and activate a virtual environment (recommended).
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    - Install the required Python packages using the provided `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit App**:
    - Start the Streamlit app.
    ```bash
    streamlit run app.py
    ```

2. **Provide Music Track**:
    - In the app, you will be prompted to input a music track title from the dataset.
    
3. **Receive Recommendations**:
    - The system will display a list of recommended tracks similar to the selected music track based on K-means clustering.

## Data

- The Spotify dataset used in this project contains music track information, including track titles, artists, and audio features such as tempo, danceability, energy, and more.
- The dataset is processed and used for building the recommendation system.

## Recommendation Algorithm

- The recommendation system employs K-means clustering to group music tracks based on their audio features and recommend similar tracks from the same cluster.
    - **K-means Clustering**: Tracks are clustered based on audio features such as tempo, danceability, energy, and more.
    - **Recommendations**: Similar tracks are recommended from the same cluster as the input track.

## Code Explanation

- **app.py**:
    - The Streamlit app script for loading the Spotify dataset and running the music recommendation system.
    - Provides a user-friendly interface for inputting a music track and receiving recommendations for similar tracks.
    - Uses K-means clustering to group tracks and recommends similar tracks from the same cluster.

## References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [K-means Clustering Explained](https://en.wikipedia.org/wiki/K-means_clustering)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Spotify API Documentation](https://developer.spotify.com/)

## Conclusion

This project provides an example of building a music recommendation system using a Spotify dataset and a Streamlit app for user interaction. By employing K-means clustering, the system can provide recommendations of similar music tracks based on user input. Feel free to customize and extend this project to suit your needs.
