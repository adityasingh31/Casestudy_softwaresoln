import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate
from surprise import accuracy

# Load data
data = pd.read_csv('user_interactions_features.csv')
reader = Reader(rating_scale=(1, 5))
dataset = Dataset.load_from_df(data[['user_id', 'item_id', 'rating']], reader)

# Train-test split
trainset, testset = train_test_split(dataset, test_size=0.2)

# Build and train model
model = SVD()
model.fit(trainset)

# Evaluate model
predictions = model.test(testset)
rmse = accuracy.rmse(predictions)

print(f"Model RMSE: {rmse}")
