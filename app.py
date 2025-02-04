import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=4b088fe2ab9d511ef1db2de6a1956660&language=en-US"
    response = requests.get(url)
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    recommended_movies=[]
    recommended_movies_poster=[]
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:7]
    for i in movies_list:
        movie_id =movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return  recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('Movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie=st.selectbox(
    "Select Movie",
    movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie)
    col1, col2, col3, col4, col5,col6 =st.columns(6)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])



