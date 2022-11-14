# Recommendation Engine

### Included in this repository:

- app directory
    - recommend_app.py -- python file for the streamlit webapp
- notbooks directory
    - data_clean_EDA -- notebook used to pull and clean data from Goodreads website
    - one_df_models -- notebook that shows the model workflow for one df (quick process)
    - recommend_eng -- notebook used to generate model and create a recommendiation system
- resources directory
    - Charts generated through EDA
- slides directory
    - Slides used for project presentation

## Problem Statement

When people decide they want to read a book (or watch a movie), it takes them hours to decide what book to read or what movie to watch. 
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
The data about authors in this dataframe was tricky as it was stored in a dictionary, with other people's names who were working on the book. So I needed to extract just the author id out of the dictionary for each book. After that, the dataframe for authors was loaded and the authors name was added to the main dataframe. Then, after checking that all the dataframes are correct, they were saved in the .csv format in the same Dataset folder. 

After setting up the dataframes, I then dove deeper into the data to analyze it. 
First, I looked at the top rated books, i.e the books that have the highest average rating for each genre: 

PIC HERE!

Then looked which books have the most amount of reviews:

PIC HERE!

Then looked at the top voted books, the books that have the most amount of ratings: 

PIC HERE!

Looked at authors who wrote the most amount of books, which gave me quite expected results: 

And looked at the top rated authors, which we can see that some of them are from the group of authors that wrote the most abount of books

Then finally, I looked at the thickest books 

Finally, the reviews and ratings dataframe was downloaded and cleaned (mostly just removed the unnecessary columns) and saved to the dataframe. 

---

## Preprocessing & Modeling




#### Web application

The preliminary app was created for the 11 most popular stations using streamlit. It lets the user choose the station, choose the date that they’re planning on traveling (for the purpose of this project, we only have data saved up to Oct, 14, so the model would work best for the week after that date). Also it lets the user choose the time they’d like to arrive at the station and the amount of passengers that are going to be traveling. As a result, the app gives the price for the trip, tells a user how many people are expected to be at the station during a chosen time slot and whether or not it is advised to travel. For the expected amount of people, we chose the prediction from our model. The criteria for how busy the station is was chosen arbitrarily. 

---

## Conclusion & Recommendations
