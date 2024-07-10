import pandas as pd
import numpy as np

# Generate synthetic data
def generate_synthetic_data():
    num_users = 1000
    num_items = 500
    ratings = []

    for user_id in range(1, num_users + 1):
        num_ratings = np.random.randint(10, 100)
        for _ in range(num_ratings):
            item_id = np.random.randint(1, num_items + 1)
            rating = np.random.randint(1, 6)
            ratings.append((user_id, item_id, rating))
    
    df = pd.DataFrame(ratings, columns=['user_id', 'item_id', 'rating'])
    df.to_csv('user_interactions.csv', index=False)

generate_synthetic_data()
print("Synthetic data generated and saved to 'user_interactions.csv'.")
