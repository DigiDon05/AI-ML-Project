import pandas as pd

# Load datasets
fake = pd.read_csv("data/Fake.csv")
true = pd.read_csv("data/True.csv")

# Add labels
fake["label"] = 1  # Fake
true["label"] = 0  # Real

# Combine datasets
data = pd.concat([fake, true])

# Keep only required columns
data = data[["text", "label"]]

# Shuffle data (important)
data = data.sample(frac=1)

# Save final dataset
data.to_csv("data/news.csv", index=False)

print("✅ news.csv created successfully!")
