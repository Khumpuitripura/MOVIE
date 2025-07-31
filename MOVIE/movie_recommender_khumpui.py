import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load datasets with correct paths
movies = pd.read_csv('C:/Users/amand/Downloads/ml-latest-small/movies.csv')
ratings = pd.read_csv('C:/Users/amand/Downloads/ml-latest-small/ratings.csv')

# Merge ratings and movies on movieId
movie_data = pd.merge(ratings, movies, on='movieId')

# Group by movie title and get average rating and number of ratings
movie_stats = movie_data.groupby('title').agg({'rating': ['mean', 'count']})
movie_stats.columns = ['average_rating', 'rating_count']
movie_stats = movie_stats.reset_index()

# Filter to only include movies with at least 50 ratings for stability
popular_movies = movie_stats[movie_stats['rating_count'] >= 50]

# Create a pivot table: rows = userId, columns = movie titles, values = ratings
movie_matrix = movie_data.pivot_table(index='userId', columns='title', values='rating')

# Fill NaN with 0 for similarity calculation
movie_matrix_filled = movie_matrix.fillna(0)

# Calculate cosine similarity between movies (transpose needed)
similarity = cosine_similarity(movie_matrix_filled.T)

# Convert similarity to a DataFrame
similarity_df = pd.DataFrame(similarity, index=movie_matrix.columns, columns=movie_matrix.columns)

# --- Function to Recommend Movies ---
def recommend_movies(movie_name, num_recommendations=5):
    if movie_name not in similarity_df.columns:
        return f"❌ Movie '{movie_name}' not found in the database."
    
    # Sort the similarity scores in descending order
    similar_scores = similarity_df[movie_name].sort_values(ascending=False)

    # Skip the first one (which will be the same movie)
    recommended_movies = similar_scores[1:num_recommendations+1]
    
    return recommended_movies

# --- Example: Recommend movies similar to 'Toy Story (1995)' ---
movie_to_search = 'Toy Story (1995)'
recommendations = recommend_movies(movie_to_search)

print(f"\n📽️ Movies similar to '{movie_to_search}':\n")
print(recommendations)
