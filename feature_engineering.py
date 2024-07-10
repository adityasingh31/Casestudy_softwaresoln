import pandas as pd

# Load data
df = pd.read_csv('user_interactions.csv')

# Feature engineering
df['interaction_count'] = df.groupby('user_id')['rating'].transform('count')
df['average_rating'] = df.groupby('user_id')['rating'].transform('mean')

df.to_csv('user_interactions_features.csv', index=False)
print("Features added and saved to 'user_interactions_features.csv'.")
