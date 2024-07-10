import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('user_interactions_features.csv')

# Example: Content filtering to ensure diversity
unique_items = data['item_id'].nunique()
diverse_recommendations = []

for user_id in data['user_id'].unique():
    user_data = data[data['user_id'] == user_id]
    recommended_items = user_data.sample(n=min(10, unique_items))['item_id'].tolist()
    diverse_recommendations.append((user_id, recommended_items))

# Save diverse recommendations
diverse_df = pd.DataFrame(diverse_recommendations, columns=['user_id', 'recommended_items'])
diverse_df.to_csv('diverse_recommendations.csv', index=False)
print("Diverse recommendations generated and saved to 'diverse_recommendations.csv'.")
