# Movie Recommendation System

## Overview
This project is a movie recommendation system that suggests similar movies based on vectorization techniques. It utilizes **CountVectorizer** and **Cosine Similarity** to analyze movie data and find recommendations. The dataset is sourced from **TMDB (The Movie Database)**.

The system works by processing movie descriptions, keywords, and metadata, transforming them into numerical vectors using **CountVectorizer**. These vectors are then compared using **Cosine Similarity** to determine how closely related two movies are. The higher the similarity score, the more relevant the recommendation.

This approach allows for content-based recommendations, meaning that users can discover movies similar to their favorites based on descriptive elements rather than user ratings or collaborative filtering techniques. It is lightweight and efficient, making it suitable for various applications, including personal use or integration into larger movie recommendation platforms.

## Features
- Recommends similar movies based on textual metadata.
- Uses **CountVectorizer** to convert text data into numerical vectors.
- Calculates **Cosine Similarity** to measure similarity between movies.
- Efficient and lightweight movie recommendation system.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- TMDB dataset

##Prerequisites
To run this Jupyter Notebook project, you need the following prerequisites:

Python (3.x recommended)
Jupyter Notebook
Required Python libraries: pandas, numpy, scikit-learn
## Data Source
The movie dataset is obtained from **TMDB (The Movie Database)**.

##Deployment

This project is deployed and can be accessed at:
🔗 Movie Recommendation System
