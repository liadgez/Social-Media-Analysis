import pandas as pd
import numpy as np
import random

# Define the list of categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']

# Number of entries (n)
n = 90000

# Generate random data
data = {
    'Date': pd.date_range('2015-01-01','2023-12-31', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n),
    'Shares': np.random.randint(0, 1000, size=n),
    'Reposts': np.random.randint(0, 200, size=n),
    'Comments': np.random.randint(0, 10000, size=n)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Split the 'Date' column into separate 'Date' and 'Time' columns
df['Date'] = df['Date'].dt.date  # Extract only the date component

df.to_csv('Twitter_Analysis.csv', index=False)

# Print the first few rows of the DataFrame
print(df.head(10))
