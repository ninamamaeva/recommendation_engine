import streamlit as st
import pandas as pd

import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import sparse

from sklearn.metrics.pairwise import pairwise_distances, cosine_similarity, cosine_distances
from sklearn.neighbors import NearestNeighbors


@st.cache
def get_genre_df(genre):
    return pd.read_json('./Dataset/'+ genre +'.csv', lines=True)

@st.cache
def get_genre_pivot_df(genre):
    return pd.read_json('./Dataset/'+genre+'_pivot.csv', lines=True)
    
@st.cache
def get_sparse_matrix(df):
    sparse_data = sparse.csr_matrix(df.fillna(0).values)
    sim_sparse = cosine_similarity(sparse_data, dense_output = False)

    rec_df = pd.DataFrame.sparse.from_spmatrix(
        sim_sparse,
        index = df.index,
        columns = df.index
    )

    return rec_df

# =================================================================================
df_poetry = get_genre_df('poetry')
df_poetry_reviews = get_genre_pivot_df('poetry')
df_poetry_recommendations = get_sparse_matrix(df_poetry_reviews)

def get_cosine_similarities(book_title, df, rec_df): 
    if df['title'].str.contains(book_title).any():
        found_book = df[df['title'].str.contains(book_title)]
        found_book_id = found_book['book_id'].iloc[0]
        found_book_title = found_book['title'].iloc[0]

        print(f"My book is {found_book_title}")

        matched_books = []
        recs = rec_df[found_book_id].sort_values(ascending = False).head(20)

        for i, v in recs.items():
            if i != found_book_id:
                match_book = df[df['book_id'] == i]    
                match_book_title = match_book['title'].iloc[0]

                matched_books.append({
                    'book_id': i,
                    'title': match_book_title,
                    'value': v
                })
        
        matches_df = pd.DataFrame(matched_books)
        return matches_df
    else:
        return False 


st.title('What to read?')
genre = ['Poetry', 'Children', 'Fantasy and Paranrmal', 'History and Biography', 'Mystery, Thriller and Crime', 'Romance', 'Young Adult', 'Comics and Graphic']
genre_extended = ['Choose below']
genre_extended.extend(sorted(genre))
search_genre = st.selectbox('Select your favorite genre', options = genre_extended)
search_title = st.text_input('Enter book title')

if search_title and search_genre != 'Choose below':
    f = get_cosine_similarities(search_title, df_poetry, df_poetry_recommendations)
    st.write(f'You searched for {search_title}')
    st.dataframe(f)


#  the keyword for the book that you recently liked:



# Create a button and print out the result:
st.button('Let\'s read!')