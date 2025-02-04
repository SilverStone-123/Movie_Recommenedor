import pandas as pd
import streamlit as st
import pickle
import requests
import numpy as np

@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=4b088fe2ab9d511ef1db2de6a1956660&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')
    return "https://via.placeholder.com/500"  

@st.cache_resource
def load_data():
    movies_dict = pickle.load(open('Movies_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return pd.DataFrame(movies_dict), similarity

movies, similarity = load_data()

def recommend(movie):
    recommended_movies = []
    recommended_movies_poster = []
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    top_indices = np.argsort(-distances)[1:7]
    movies_list = [(i, distances[i]) for i in top_indices]

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster

st.title('🎬 Movie Recommender System')
selected_movie = st.selectbox("Select a Movie", movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    cols = st.columns(6)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)


