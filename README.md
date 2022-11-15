# Recommendation Engine

### Included in this repository:

- app directory:
    - recommend_app.py -- python file for the streamlit webapp
- notbooks:
    - data_clean_EDA -- notebook used to pull and clean data from Goodreads website
    - one_df_models -- notebook that shows the model workflow for one df (quick process)
    - recommend_eng -- notebook used to generate model and create a recommendiation system
- resources directory
    - charts generated through EDA
- slides:
    - slides used for project presentation

## Problem Statement

When people decide they want to read a book, it takes them hours to decide what book to read as there are so many of them. According to Statista, books sales are holding steady at 650 million units per year. When it comes to publishing, figures range from 500,000 to one million books published annually.
Here's where recommendation system come into play. It offers a user relevant suggestions based on previous experience. For instance Facebook/Instagram knows what kind of adds to suggest or YouTube suggests a videos that you might like based on your search/watch and purchase history. 

In this project, I built the recommendation engine that suggests the books based on the keywpord of a previously read book. 

---
Planned steps for the implementation of the project:
Download all necessary data from Goodreads website
Conduct basic data check and EDA
Create a cosine similarities and NearesrtNeighbor recommensation models
Develop a basic webapp to check usability of the model for book suggestions

---

## Data Collection

There are 8 datasets that were used for this project. One for each genre (Poetry, Children, History and Biography, Mystery Thriller and Crime, Young Adult, Comics and Graphic).

There are two more datasets that can be downloaded and added to the project, but they're quite large (Romance, Fantasy and Paranormal). 

These genre dataframes were pulled from the [UCSD](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home), which were collected in late 2017 from [goodreads.com](https://www.goodreads.com/). 
These datasets contain book information, but only author id, so author information as well as the ratings and reviews datasets hve to be downloaded separately. It can be done form the same page mentioned above. 

---

## Data Cleaning & EDA

The data from the UCSD website is quite complete, so there was no need to adress any null values. The fist step was to delete all the unnecessary colunms from the dataframe, such as URL, edition information, asin, is e-book etc. Then, for each genre dataframe we'll add a column with the name of the genre for future use. 
The data about authors in this dataframe was tricky as it was stored in a dictionary, with other people's names who were working on the book. So I needed to extract just the author id out of the dictionary for each book. I noticed that there are a couple of books in the fantasy genre were missing information about the author, so I had to go on the goodreads website and find these books. They were the collevtion of stories, so for the first one I used the author whos work the book is about (of grandmaster H. Warner Munn), for the second book, I serached the the book name and took the first books author's name. After that, the dataframe for authors was loaded and the authors name was added to the main dataframes. 
Then, after checking that all the dataframes are correct, they were saved in the .csv format in the same Dataset folder. 

After setting up the dataframes, I then dove deeper into the data to analyze it. 
First, I looked at the top rated books, i.e the books that have the highest average rating for each genre: 

|Genre|Book|
|---|---|
|Children| |
|Poetry| |
|History and Biography| |
|Mystery, Thriller and Crime| |
|Young Adult| |
|Comics and Graphic| |
|Romance| |
|Fantasy and Paranormal| |

Then looked which books have the most amount of reviews:

|Genre|Book|
|---|---|
|Children| |
|Poetry| |
|History and Biography| |
|Mystery, Thriller and Crime| |
|Young Adult| |
|Comics and Graphic| |
|Romance| |
|Fantasy and Paranormal| |

Then looked at the top voted books, the books that have the most amount of ratings: 

|Genre|Book|
|---|---|
|Children| |
|Poetry| |
|History and Biography| |
|Mystery, Thriller and Crime| |
|Young Adult| |
|Comics and Graphic| |
|Romance| |
|Fantasy and Paranormal| |

Looked at authors who wrote the most amount of books, which gave me quite expected results: 

And looked at the top rated authors, which we can see that some of them are from the group of authors that wrote the most abount of books

Then finally, I looked at the thickest books 

Finally, the reviews and ratings dataframe was downloaded and cleaned (mostly just removed the unnecessary columns) and saved to the dataframe. 

---

## Preprocessing & Modeling

For the recommendation engine  first used cosine similarity, which worked. Then for simplicity or building an app, I decided to use the nearest neighbors algorithm which is the same as K nearest which is used for clustering based on euclidian distance.
We used content-based filtering, whcich is mainly based on the description of the product or the keywords of the name of the product. Which means if you liked a book in category 'X', you will get recommendations to read books from the same category only. 
For this model, I used nearest neighbor model with metric cosine and the algorithm 'brute', which means find the distance of every point to every other point. In order to match the book (keyword) with the existing books in the data sets, I used FuzzyWuzzy Library that amkes string matching very simple. I used the process module to only extract one string with the highest similarity score by calling the extractOne() function. Then, the model finds the nearest neighbors to the input book id and after that, it will print the top 10 books which are closer to those books.

    Installing FuzzyWuzzy:
    pip install fuzzywuzzy

As it can be seen from the code, I used both cosine and nearest neighbors approaches. These two gave out different results, which is expected. But there's no way to check if it is correct since it's unsupervised modelling. 

#### Web application

The preliminary app was created for each genre using streamlit. It lets the user choose the genre and enter the name of the book they recentry liked or the keyword that the title of that book has. As a result, the app gives the full title of the selected book, and the list of books that are the closest to the book mentioned by the user. It also gives the book id and the authors names for each suggested book. 

---

## Conclusion & Recommendations

The recommendation engine can successfully give suggestions on the books from 8 different genres. 
The app that was developed can be used for a simpler user interface. 
For future work, it would be nice to do this recommendation app based on the description of the book. For example the user would like to read about 'war' and it would suggest the books that are about war. Also there's a large dataset that was conveniently broken down into smaller datasets (by genre) for faster usage, but it would be interesting to see if the recommendation engine would work differently on the bigger dataset. In these smaller (genre) datasets there are about 40% of books that don't have the description at all, so this information will have to be scraped manually from somewhere else. 
Also, I used the books written in all languages, but it would be nice to remove the books that are not in english and leave the books that are in english only. It will take some time as well, since a lot of the books don't have information about the language they're written in, also the reviews and ratings datasets would have to be cleanned from the same list of books, so that the amount of books are the same in all datasets. 

