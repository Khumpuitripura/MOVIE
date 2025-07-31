PROJECT TITLE: Movie Recommendation System

DESCRIPTION:
A simple content-based movie recommender system built using Python. It recommends similar movies based on the input movie's genres and features using cosine similarity.

TECHNOLOGIES USED:
- Python
- Pandas
- scikit-learn
- Streamlit (for interactive UI)

DATASET USED:
- File: movies.csv
- Source: MovieLens (https://grouplens.org/datasets/movielens/)
- Location: ./Downloads/ml-latest-small/movies.csv

FEATURES:
- Content-based filtering using genre metadata
- Cosine similarity for movie similarity measurement
- Streamlit-based web interface to search and get top 5 similar movies

HOW TO RUN:
1. Ensure pandas, scikit-learn, and streamlit are installed.
2. Run the recommender with: streamlit run movie_recommender_khumpui.py
3. Enter a movie title to receive recommendations.

PROJECT STRUCTURE:
- movie_recommender_khumpui.py → Main app
- Downloads/ml-latest-small/movies.csv → Dataset
- requirements.txt → Libraries required

AUTHOR: Khumpui Tripura
YEAR: 2025
