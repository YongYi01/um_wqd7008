# Step 1: Data Exploration

# Import necessary libraries
import pandas as pd

# Load the dataset
data_path = '/home/ubuntu/project/um_wqd7008/hourly_weather.csv'
df = pd.read_csv(data_path)

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst Few Rows of the Dataset:")
print(df.head())
