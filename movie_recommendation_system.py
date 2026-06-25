import numpy as np
import pandas as pd
import ast as ast
import sklearn
import nltk

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

movies.head()
credits.head()

movies = movies.merge(credits,on='title')

#only using the useful columns like
#genres
#id
#keywords
#title
#overview
#cast
#crew

movies = movies[['movie_id', 'title','overview', 'genres', 'keywords', 'cast', 'crew']]
movies.head()

#finding missing data
movies.isnull().sum()

#removing missing data
movies.dropna(inplace=True)

#removing duplicate data
movies.duplicated().sum()

#formatting columns
#for genres
movies.iloc[0].genres

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)


#for keywords
movies['keywords'] = movies['keywords'].apply(convert)

#for cast
def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L

movies['cast'] = movies['cast'].apply(convert3)

#crew
def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

movies['crew'] = movies['crew'].apply(fetch_director)

#converting the string value of overview column into list 
movies['overview'] = movies['overview'].apply(lambda x:x.split())

#removing spaces 
movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

movies.head()

#creating tags
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

new_df = movies[['movie_id','title','tags']].copy()


#converting into strings again
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

new_df.head()

#stemming 
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)
    
new_df['tags'] = new_df['tags'].apply(stem)

#vectorization 
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words = 'english')
vectors = cv.fit_transform(new_df['tags']).toarray()

cv.get_feature_names_out()

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

sorted(list(enumerate(similarity[0])),reverse=True, key=lambda x:x[1])[1:6]

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)
        
    
recommend('Avatar')

new_df.iloc[1216].title

import pickle
pickle.dump(new_df,open('movies.pkl','wb'))

new_df['title'].values

pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))