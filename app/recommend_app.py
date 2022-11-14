import streamlit as st
import pandas as pd

import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import sparse
import pickle
from fuzzywuzzy import process

from sklearn.metrics.pairwise import pairwise_distances, cosine_similarity, cosine_distances
from sklearn.neighbors import NearestNeighbors

@st.cache
def get_genre_df(genre):
    return pd.read_csv('./models/'+ genre +'.csv')

@st.cache
def get_genre_reviews_matrix(genre):
    df = pd.read_csv('./models/'+genre+'_rev.csv')
    poetry_reviews = df.pivot_table(index='book_id', values='rating').fillna(0)
    return sparse.csr_matrix(poetry_reviews.values)   

@st.cache
def load_model():
    return pickle.load(open('./models/poetry_knn_model.pkl','rb'))

def get_knn(book_title, data, review_data):
    model = load_model()

    book_idx = process.extractOne(book_title, data['title'])[2]
    print('Selected book: ',data['title'][book_idx])
    
    matched_books = []
    indices = model.kneighbors(review_data[book_idx], n_neighbors=10)[1]

    for i in indices[0]:
        if i != book_idx:  
            matched_books.append({
                'book_id': data['book_id'][i],
                'title': data['title'][i],
                'author': data['author_name'][i]
            })
        
    matches_df = pd.DataFrame(matched_books)
    return matches_df, data['title'][book_idx]



# start program
df_children = get_genre_df('children')
df_comics = get_genre_df('comics')
df_history = get_genre_df('history')
df_mystery = get_genre_df('mystery')
df_poetry = get_genre_df('poetry')
df_adult = get_genre_df('young_adult')

mat_children_reviews = get_genre_reviews_matrix('children')
mat_comics_reviews = get_genre_reviews_matrix('comics')
mat_history_reviews = get_genre_reviews_matrix('history')
mat_mystery_reviews = get_genre_reviews_matrix('mystery')
mat_poetry_reviews = get_genre_reviews_matrix('poetry')
mat_adult_reviews = get_genre_reviews_matrix('adult')

# show ui

st.title('What to read?')
genre = ['Poetry', 'Children', 'History and Biography', 'Mystery, Thriller and Crime', 'Young Adult', 'Comics and Graphic']
genre_extended = ['Choose below']
genre_extended.extend(sorted(genre))
search_genre = st.selectbox('Select your favorite genre', options = genre_extended)
search_title = st.text_input('Enter book title keyword')

if search_title and search_genre != 'Choose below':
    if search_genre == 'Poetry':
        df, searched_book = get_knn(search_title, df_poetry, mat_poetry_reviews)
    elif search_genre == 'Chilren':
        df, searched_book = get_knn(search_title, df_children, mat_children_reviews)
    elif search_genre == 'History and Biography':
        df, searched_book = get_knn(search_title, df_history, mat_history_reviews)
    elif search_genre == 'Mystery, Thriller and Crime':
        df, searched_book = get_knn(search_title, df_mystery, mat_mystery_reviews)
    elif search_genre == 'Young Adult':
        df, searched_book = get_knn(search_title, df_adult, mat_adult_reviews)
    elif search_genre == 'Comics and Graphic': 
        df, searched_book = get_knn(search_title, df_comics, mat_comics_reviews)   

    st.write(f'You searched for {search_title}')
    st.write('Most similar book: ', searched_book)
    st.dataframe(df)


# Create a button and print out the result:
st.button('Let\'s read!')