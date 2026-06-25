import streamlit as st
import pandas as pd
import requests
import pickle

# -------------------------------
# TMDB API CREDENTIALS
# -------------------------------
TMDB_V3_API_KEY = 'b8ac026cea88249f1f90a4f845ac1b73'
TMDB_V4_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOGFjMDI2Y2VhODgyNDlmMWY5MGE0Zjg0NWFjMWI3MyIsIm5iZiI6MTc1MjY3MTgzOC4zMTAwMDAyLCJzdWIiOiI2ODc3YTY1ZTEyMTMyNDkxNGYxNjVkMjQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.AvpdYmtTUzfH8dF6aEGlGbd3miJ2cEWR-QSr8kuVjto'

# -------------------------------
# FETCH POSTER FROM TMDB API
# -------------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {TMDB_V4_TOKEN}",
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500" + poster_path
            return full_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

# -------------------------------
# LOAD DATA
# -------------------------------
# Load movie dataframe
new_df_dict = pickle.load(open('movie_dict.pkl', 'rb'))
new_df = pd.DataFrame(new_df_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# -------------------------------
# RECOMMENDATION FUNCTION
# -------------------------------
def recommend(movie_title):
    try:
        movie_index = new_df[new_df['title'] == movie_title].index[0]
    except IndexError:
        return [], []

    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in movies_list:
        movie_id = new_df.iloc[i[0]].movie_id
        title = new_df.iloc[i[0]].title
        poster_url = fetch_poster(movie_id)

        recommended_titles.append(title)
        recommended_posters.append(poster_url)

    return recommended_titles, recommended_posters

# -------------------------------
# CUSTOM CSS AND ANIMATION
# -------------------------------
custom_css = """
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
<style>
body {
    background: linear-gradient(135deg, #1f1c2c, #928DAB);
    font-family: 'Poppins', sans-serif;
    color: #ffffff;
}
h1 {
    text-align: center;
    font-size: 3em;
    background: linear-gradient(270deg, #ff6ec4, #7873f5, #4adede, #ff6ec4);
    background-size: 800% 800%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 10s ease infinite;
}
@keyframes glow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.css-18e3th9 {
    color: #FFC107;
    font-weight: bold;
    font-size: 1.1em;
}
img {
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.5);
    transition: transform 0.3s ease;
}
img:hover {
    transform: scale(1.08);
}
.css-1cpxqw2 {
    color: #ffffff;
    font-size: 1em;
    font-weight: bold;
    text-align: center;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# -------------------------------
# STREAMLIT UI
# -------------------------------
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    new_df['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    if names:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.image(posters[idx], use_column_width=True)
                st.caption(names[idx])
    else:
        st.write("No recommendations found.")