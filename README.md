# Music Recommendation System

This project demonstrates how to build a music recommendation system using a Spotify dataset. The system employs the cosine similarity algorithm and TF-IDF vectorizer to recommend similar music tracks based on the content of track descriptions. Additionally, it includes a Streamlit app that provides a user-friendly interface for inputting a track and receiving recommendations for similar tracks.

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

The music recommendation system suggests similar music tracks based on the content of track descriptions from a Spotify dataset. The system uses a combination of TF-IDF vectorization and cosine similarity to calculate the similarity between track descriptions and provide recommendations.

The project includes a Streamlit app that provides a user-friendly interface for inputting a music track and receiving recommendations for similar tracks.

## Features

- Uses a Spotify dataset for music recommendations.
- Implements TF-IDF vectorizer for text representation.
- Uses cosine similarity to calculate similarity between music tracks.
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
    - The system will display a list of recommended tracks similar to the selected music track.

## Data

- The Spotify dataset used in this project contains music track information, including track titles, artists, and descriptions.
- The dataset is processed and used for building the recommendation system.

## Recommendation Algorithm

- The recommendation system employs the following methods:
    - **TF-IDF Vectorization**: Text descriptions of music tracks are transformed into numerical vectors using Term Frequency-Inverse Document Frequency (TF-IDF) vectorization.
    - **Cosine Similarity**: Cosine similarity is calculated between the input music track and all other tracks based on their TF-IDF vectors to find the most similar tracks.

## Code Explanation

- **app.py**:
    - The Streamlit app script for loading the Spotify dataset and running the music recommendation system.
    - Provides a user-friendly interface for inputting a music track and receiving recommendations for similar tracks.
    - Uses TF-IDF vectorization to transform music track descriptions into vectors and calculates cosine similarity to recommend similar tracks.

## References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Cosine Similarity Explained](https://en.wikipedia.org/wiki/Cosine_similarity)
- [TF-IDF Explained](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Spotify API Documentation](https://developer.spotify.com/)

## Conclusion

This project provides an example of building a music recommendation system using a Spotify dataset and a Streamlit app for user interaction. By employing TF-IDF vectorization and cosine similarity, the system can provide recommendations of similar music tracks based on user input. Feel free to customize and extend this project to suit your needs.
